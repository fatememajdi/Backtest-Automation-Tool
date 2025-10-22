import re
from typing import Dict, Any, Optional
import numpy as np
import pandas as pd
import requests
import json


def GetCompanyData(company_id, domain, company_domain):
    """
    Sends a POST request to the given domain to fetch all diagnostic information
    for the specified company and returns the response as JSON.
    """
    url = f"http://{domain}:4000/alldiagnosisinformations"
    headers = {
        "api-key": "e8i3jDdaemYZNtPDTlgE5kLfIbu"
    }

    input_data = {
        'CompanyId': company_id,
        'SelectedDate': '',
        "domain": company_domain
    }

    try:
        res = requests.post(url=url, json=input_data,
                            headers=headers, timeout=30)
        print("Status code:", res.status_code)

        if res.status_code == 200:
            try:
                # with open(f'/Users/fateme/Desktop/CeeNous/Backtest Automation/data/response_{company_domain}.json', "w", encoding="utf-8") as f:
                #     json.dump(res.json(), f, ensure_ascii=False, indent=2)
                return res.json()
            except json.JSONDecodeError:
                print("Invalid JSON response")
                return None
        else:
            print(f"Request failed: {res.status_code} - {res.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error in GetCompanyData: {e}")
        return None


def _normalize(val):
    """Normalize a value to a trimmed string or empty string if None."""
    if val is None:
        return ""
    return str(val).strip()


def find_post_entry(post_json: Dict[str, Any], tag: str, date: str, spare: str, point: str) -> Optional[Dict[str, Any]]:
    """
    Try to find a matching entry in post_json for given tag/date/spare/point.
    Returns the first matching dict or None.
    """
    tag_n = _normalize(tag)
    date_n = _normalize(date)
    spare_n = _normalize(spare)
    point_n = _normalize(point)

    if tag_n not in post_json:
        return None
    if date_n not in post_json[tag_n]:
        return None
    for rec in post_json[tag_n][date_n]:
        if _normalize(rec.get("Tag")) and _normalize(rec.get("Tag")) != tag_n:
            continue
        if _normalize(rec.get("SparePart")) and _normalize(rec.get("SparePart")) != spare_n:
            continue
        rec_point = _normalize(rec.get("Point", ""))
        if rec_point and point_n and rec_point != point_n:
            continue
        return rec
    return None


def _extract_chart_key(chartplot: str, tag: str):
    """
    Extracts the key components (e.g. M-1-H or PUMP-4-H) from a ChartPlot filename
    by removing the machine tag prefix and capturing the pattern with regex.
    """
    if not chartplot:
        return ""
    chartplot = chartplot.strip()

    if chartplot.startswith(tag):
        chartplot = chartplot[len(tag):].lstrip('-')

    match = re.search(r'([A-Za-z]+)-(\d+)-([A-Za-z])', chartplot)
    if match:
        return "-".join(match.groups()).upper()
    return ""


def build_excel_multilevel(pre_json, post_json, output_path):
    """
    Builds an Excel file that compares pre-test and post-test diagnostic data.
    It validates failure modes, probabilities, and chart similarity, then saves
    results in a multi-level column Excel report.
    """

    def _safe_float(x):
        """Safely convert a value to float; returns np.nan if invalid."""
        try:
            if x in [None, "", "-", "nan", "NaN"]:
                return np.nan
            return float(x)
        except:
            return np.nan

    def _norm(x):
        """Normalize string values inside nested functions."""
        return "" if x is None else str(x).strip()

    def find_post(tag, date, spare, point):
        """Find corresponding post-test record by tag/date/spare/point."""
        tag, date, spare, point = map(_norm, [tag, date, spare, point])
        if tag not in post_json or date not in post_json[tag]:
            return None
        for r in post_json[tag][date]:
            if _norm(r.get("SparePart")) == spare and _norm(r.get("Point")) == point:
                return r
        return None

    rows = []
    for tag, date_dict in pre_json.items():
        for date, records in date_dict.items():
            for rec in records:
                machine = _norm(rec.get("Tag", tag))
                part = _norm(rec.get("SparePart"))
                point = _norm(rec.get("Point"))
                failure = _norm(rec.get("FailureDiagnosis"))
                date_ = _norm(rec.get("SelectedDate", date))
                chart_pre = _norm(rec.get("ChartPlot"))
                prob_pre = _safe_float(rec.get("Probability"))
                prediction = "Healthy" if failure.lower() == "no failure detected" else "Faulty"

                post = find_post(tag, date, part, point)
                if post:
                    failure_post = _norm(post.get("FailureDiagnosis"))
                    prob_post = _safe_float(post.get("Probability"))
                    chart_post = _norm(post.get("ChartPlot"))
                else:
                    failure_post = ""
                    prob_post = np.nan
                    chart_post = ""

                failure_val = True if failure_post and failure_post.lower() == failure.lower() else False

                if np.isnan(prob_pre) and np.isnan(prob_post):
                    intensity_val = True
                elif np.isnan(prob_pre) or np.isnan(prob_post):
                    intensity_val = False
                else:
                    intensity_val = abs(prob_pre - prob_post) <= 15

                chart_pre_key = _extract_chart_key(chart_pre, machine)
                chart_post_key = _extract_chart_key(chart_post, machine)
                worst_val = chart_pre_key == chart_post_key if chart_post_key else False

                if not failure_val:
                    intensity_val = False
                    worst_val = False

                rows.append([
                    machine, failure, part, point, date_,
                    prediction,
                    failure_val, _norm(
                        post.get('AIFeedbackNote')if post else ""),
                    intensity_val, "",
                    worst_val, ""
                ])

    header = pd.MultiIndex.from_tuples([
        ("", "Machine"),
        ("", "Failure Mode"),
        ("", "Part"),
        ("", "Point / Spare"),
        ("", "Date"),
        ("", "Prediction"),
        ("Failure", "Validation"),
        ("Failure", "Description"),
        ("Human Evaluation", "Validation"),
        ("Human Evaluation", "Description"),
        ("Worst Signal", "Validation"),
        ("Worst Signal", "Description"),
    ])

    df = pd.DataFrame(rows, columns=header)
    df.to_excel(output_path)
    return df


def BackTestAuto(company_id, company_domain_before_backtest, company_domain_after_backtest, output_path, domain='20.108.64.195'):
    """
    Runs the automated backtest process:
    1. Fetches pre-test and post-test data from server.
    2. Compares them and generates an Excel report using build_excel_multilevel().
    """
    data_before_backtest = GetCompanyData(
        company_id, domain, company_domain_before_backtest)

    data_after_backtest = GetCompanyData(
        company_id, domain, company_domain_after_backtest)

    if data_before_backtest is None or data_after_backtest is None:
        print("No data fetched. Exiting.")
        return

    build_excel_multilevel(
        pre_json=data_before_backtest,
        post_json=data_after_backtest,
        output_path=output_path
    )

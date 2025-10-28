# Library
import pandas as pd
from turtle import *
import colorsys
import json
# from path_handler import INFO_JSON_PATH

""" 
      "with_harmonica": {'1X_looseness' : 10,'2X_looseness' : 10,'3X_looseness' : 5,'4X_looseness' : 5,'5X_looseness' : 5, '3X_10X_RMS' : 10,
                '(3X_4X_5X)/All_X' : 10,
                'sine_wave' : 10,
                'Amplitude_ISO' : 7, 'Amplitude_ISO_1X' : 5, 'Amplitude_ISO_2X' : 5, 'Amplitude_ISO_3X' : 3, 'Amplitude_ISO_4X' : 3, 'Amplitude_ISO_5X' : 3, 'Amplitude_ISO_idx_3X_10X_RMS' : 40,
                'Direction_Sequence' : 10, 'Direction_Sequence_1X' : 10, 'Direction_Sequence_2X' : 10, 'Direction_Sequence_3X' : 4, 'Direction_Sequence_4X' : 4, 'Direction_Sequence_5X' : 4, 'Direction_Sequence_3X_10X_RMS' : 10,
                'Trend_Amplitude_Angle' : 10, 'Trend_Amplitude_Angle_1X' : 10, 'Trend_Amplitude_Angle_2X' : 10, 'Trend_Amplitude_Angle_3X' : 2, 'Trend_Amplitude_Angle_4X' : 2, 'Trend_Amplitude_Angle_5X' : 2, 'Trend_Amplitude_Angle_3X_10X_RMS' : 10,
                'Trend_Amplitude_Trend_flag' : 5, 'Trend_Amplitude_Trend_1X_flag' : 7, 'Trend_Amplitude_Trend_2X_flag' : 7, 'Trend_Amplitude_Trend_3X_flag' : 2, 'Trend_Amplitude_Trend_4X_flag' : 2, 'Trend_Amplitude_Trend_5X_flag' : 2, 'Trend_Amplitude_Trend_3X_10X_RMS_flag' : 10,
                'Trend_Constant_Slope_flag' : 5, 'Trend_Constant_Slope_1X_flag' : 7, 'Trend_Constant_Slope_2X_flag' : 7, 'Trend_Constant_Slope_3X_flag' : 2, 'Trend_Constant_Slope_4X_flag' : 2, 'Trend_Constant_Slope_5X_flag' : 2, 'Trend_Constant_Slope_3X_10X_RMS_flag' : 10,
                'Focus_Direction_Vel' : 5, 'Focus_Direction_1X' : 8, 'Focus_Direction_2X' : 8, 'Focus_Direction_3X' : 2, 'Focus_Direction_4X' : 2, 'Focus_Direction_5X' : 2, 'Focus_Direction_3X_10X_RMS' : 10},
      "without_harmonica": {'1X_looseness' : 10,'2X_looseness' : 10,'3X_looseness' : 5,'4X_looseness' : 5,'5X_looseness' : 5, '3X_10X_RMS' : 10,
                '(3X_4X_5X)/All_X' : 10,
                'sine_wave' : 10,
                'Amplitude_ISO' : 7, 'Amplitude_ISO_1X' : 5, 'Amplitude_ISO_2X' : 5, 'Amplitude_ISO_3X' : 3, 'Amplitude_ISO_4X' : 3, 'Amplitude_ISO_5X' : 3, 'Amplitude_ISO_idx_3X_10X_RMS' : 40,
                'Direction_Sequence' : 10, 'Direction_Sequence_1X' : 10, 'Direction_Sequence_2X' : 10, 'Direction_Sequence_3X' : 4, 'Direction_Sequence_4X' : 4, 'Direction_Sequence_5X' : 4, 'Direction_Sequence_3X_10X_RMS' : 10,
                'Trend_Amplitude_Angle' : 10, 'Trend_Amplitude_Angle_1X' : 10, 'Trend_Amplitude_Angle_2X' : 10, 'Trend_Amplitude_Angle_3X' : 2, 'Trend_Amplitude_Angle_4X' : 2, 'Trend_Amplitude_Angle_5X' : 2, 'Trend_Amplitude_Angle_3X_10X_RMS' : 10,
                'Trend_Amplitude_Trend_flag' : 5, 'Trend_Amplitude_Trend_1X_flag' : 7, 'Trend_Amplitude_Trend_2X_flag' : 7, 'Trend_Amplitude_Trend_3X_flag' : 2, 'Trend_Amplitude_Trend_4X_flag' : 2, 'Trend_Amplitude_Trend_5X_flag' : 2, 'Trend_Amplitude_Trend_3X_10X_RMS_flag' : 10,
                'Trend_Constant_Slope_flag' : 5, 'Trend_Constant_Slope_1X_flag' : 7, 'Trend_Constant_Slope_2X_flag' : 7, 'Trend_Constant_Slope_3X_flag' : 2, 'Trend_Constant_Slope_4X_flag' : 2, 'Trend_Constant_Slope_5X_flag' : 2, 'Trend_Constant_Slope_3X_10X_RMS_flag' : 10,
                'Focus_Direction_Vel' : 5, 'Focus_Direction_1X' : 8, 'Focus_Direction_2X' : 8, 'Focus_Direction_3X' : 2, 'Focus_Direction_4X' : 2, 'Focus_Direction_5X' : 2, 'Focus_Direction_3X_10X_RMS' : 10}
    },
    {'sine_wave' : 20,
                '3X_10X_RMS' : 0,
                '(1X_2X_3X)/All_X' : 30,
                '1X_misalignment' : 30,'2X_misalignment' : 30,'3X_misalignment' : 30,
                'Amplitude_ISO' : 0, 'Amplitude_ISO_1X' : 0, 'Amplitude_ISO_2X' : 0, 'Amplitude_ISO_3X' : 0,
                'Direction_Sequence' : 5, 'Direction_Sequence_1X' : 5, 'Direction_Sequence_2X' : 5, 'Direction_Sequence_3X' : 5,
                'Direction_Ratio' : 5, 'Direction_Ratio_1X' : 5, 'Direction_Ratio_2X' : 5, 'Direction_Ratio_3X' : 5,
                'Trend_Amplitude_Angle' : 0, 'Trend_Amplitude_Angle_1X' : 0, 'Trend_Amplitude_Angle_2X' : 0, 'Trend_Amplitude_Angle_3X' : 0,
                'Trend_Amplitude_Trend_flag' : 0, 'Trend_Amplitude_Trend_1X_flag' : 0, 'Trend_Amplitude_Trend_2X_flag' : 0, 'Trend_Amplitude_Trend_3X_flag' : 0,
                'Trend_Constant_Slope_flag' : 0, 'Trend_Constant_Slope_1X_flag' : 0, 'Trend_Constant_Slope_2X_flag' : 0, 'Trend_Constant_Slope_3X_flag' : 0,
                'Focus_Direction_Vel' : 5, 'Focus_Direction_1X' : 5, 'Focus_Direction_2X' : 5, 'Focus_Direction_3X' : 5}
                }
 """
# Static Data


# "Misalignment" :{ 'Parallel' : {'1X_score' : 10,'2X_score' : 10,'3X_score' : 10,'4X_score' : 5,'5X_score' : 5,
        #               'sine_wave' : 0, '1X_2X_3X/harmonicas' : 15, 'MW' : 20,
        #               'Amplitude_ISO_Vel_rms' : 10, 'Amplitude_ISO_Crest_rms' : 10, 'Amplitude_Similar_Vel_rms' : 10, 'Amplitude_Similar_Crest_rms' : 10,
        #               'Direction_Sequence_Vel_rms' : 10, 'Direction_Sequence_1X' : 10, 'Direction_Sequence_2X' : 20, 'Direction_Sequence_3X' : 10,
        #               'Direction_Ratio_Vel_rms' : 10, 'Direction_Ratio_1X' : 10, 'Direction_Ratio_2X' : 20, 'Direction_Ratio_3X' : 10,
        #               'Angle_Vel_rms' : 0, 'Angle_1X' : 0, 'Angle_2X' : 0, 'Angle_3X' : 0,
        #               'Trend_Vel_rms' : 0, 'Trend_1X' : 0, 'Trend_2X' : 0, 'Trend_3X' : 0,
        #               'Constant_Slope_Vel_rms' : 0, 'Constant_Slope_1X' : 0, 'Constant_Slope_2X' : 0, 'Constant_Slope_3X' : 0,
        #               'Focus_Vel_rms' : 10, 'Focus_1X' : 10, 'Focus_2X' : 20, 'Focus_3X' : 20}},
    #               'Angular' : {'1X_score' : 10,'2X_score' : 20,'3X_score' : 10,
        #               'sine_wave' : 10, '1X_2X_3X/harmonicas' : 10, 'MW' : 20,
        #               'Amplitude_ISO_Vel_rms' : 5, 'Amplitude_ISO_Crest_rms' : 0, 'Amplitude_Similar_Vel_rms' : 0, 'Amplitude_Similar_Crest_rms' : 0,
        #               'Direction_Sequence_Vel_rms' : 10, 'Direction_Sequence_1X' : 10, 'Direction_Sequence_2X' : 20, 'Direction_Sequence_3X' : 10,
        #               'Direction_Ratio_Vel_rms' : 10, 'Direction_Ratio_1X' : 10, 'Direction_Ratio_2X' : 20, 'Direction_Ratio_3X' : 10,
        #               'Angle_Vel_rms' : 0, 'Angle_1X' : 0, 'Angle_2X' : 0, 'Angle_3X' : 0,
        #               'Trend_Vel_rms' : 0, 'Trend_1X' : 0, 'Trend_2X' : 0, 'Trend_3X' : 0,
        #               'Constant_Slope_Vel_rms' : 0, 'Constant_Slope_1X' : 0, 'Constant_Slope_2X' : 0, 'Constant_Slope_3X' : 0,
        #               'Focus_Vel_rms' : 10, 'Focus_1X' : 10, 'Focus_2X' : 20, 'Focus_3X' : 20}}}





Detail = {
  "equipment_type": {"type" : "Fan" , "kind" :  "center_hung"
                    },
  "power": "group_1",
  "foundation": "rigid",
  "rpm": {"1" : {"reference": "Fix","value": 990},
          "2" : {"reference": "Fix","value": 990},
          "3" : {"reference": "Fix","value": 990},
          "4" : {"reference": "Fix","value": 990},
          "5" : {"reference": "Fix","value": 990},
          "6" : {"reference": "Fix","value": 990},
          "7" : {"reference": "Fix","value": 990},
          "8" : {"reference": "Fix","value": 990},
        },
  "Machine_part": { "M" : ["1", "2"], "F" : ["3", "4"]},
  "Customer_failure_weight": {
        "Unbalance": {
            "high_rpm": {
                "1X_score": 0,
                "sine_wave": 10,
                "1X/harmonica": 10,
                "1X/Overall": 10,
                "Amplitude_ISO_Vel_rms": 5,
                "Amplitude_ISO_Crest_rms": 5,
                "Amplitude_Similar_Vel_rms": 10,
                "Amplitude_Similar_Crest_rms": 0,
                "Direction_Sequence_Vel_rms": 4,
                "Direction_Sequence_1X": 4,
                "Direction_Ratio_Vel_rms": 4,
                "Direction_Ratio_1X": 4,
                "Angle_Vel_rms": 2,
                "Angle_1X": 2,
                "Trend_Vel_rms": 2,
                "Trend_1X": 2,
                "Constant_Slope_Vel_rms": 2,
                "Constant_Slope_1X": 2,
                "Focus_Vel_rms": 2,
                "Focus_1X": 2
            },
            "mid_rpm": { 
                # minimum RPM: 300
                # Vibration score:
                # Trend RMS -> More Sensitivity
                # Trend Crest -> low confidence -> if low, accurate intensity
                '1X_score' : 0,
                'sine_wave' : 15, # Check after backtest
                '1X/harmonica' : 10, 
                '1X/Overall' : 15, # Check after backtest
                'Amplitude_ISO_Vel_rms' : 2, 
                'Amplitude_ISO_Crest_rms' : 0,
                'Amplitude_Similar_Vel_rms' : 7,
                'Amplitude_Similar_Crest_rms' : 0,
                'Direction_Sequence_Vel_rms' : 4, 
                'Direction_Sequence_1X' : 4, 
                'Direction_Ratio_Vel_rms' : 4, 
                'Direction_Ratio_1X' : 4,
                'Angle_Vel_rms' : 4, # Check after backtest
                'Angle_1X' : 4, # Check after backtest
                'Trend_Vel_rms' : 5,
                'Trend_1X' : 5,
                'Constant_Slope_Vel_rms' : 2, # Check in backtest
                'Constant_Slope_1X' : 2,
                'Focus_Vel_rms' : 2, 
                'Focus_1X' : 2
            },
            "low_rpm": { 
                # minimum RPM: 300
                # Vibration score:
                # Trend RMS -> More Sensitivity
                # Trend Crest -> low confidence -> if low, accurate intensity
                '1X_score' : 0,
                'sine_wave' : 15, # Check after backtest
                '1X/harmonica' : 10, 
                '1X/Overall' : 15, # Check after backtest
                'Amplitude_ISO_Vel_rms' : 2, 
                'Amplitude_ISO_Crest_rms' : 0,
                'Amplitude_Similar_Vel_rms' : 7,
                'Amplitude_Similar_Crest_rms' : 0,
                'Direction_Sequence_Vel_rms' : 4, 
                'Direction_Sequence_1X' : 4, 
                'Direction_Ratio_Vel_rms' : 4, 
                'Direction_Ratio_1X' : 4,
                'Angle_Vel_rms' : 4, # Check after backtest
                'Angle_1X' : 4, # Check after backtest
                'Trend_Vel_rms' : 5,
                'Trend_1X' : 5,
                'Constant_Slope_Vel_rms' : 2, # Check in backtest
                'Constant_Slope_1X' : 2,
                'Focus_Vel_rms' : 2, 
                'Focus_1X' : 2
            },
        },
        "Looseness": {
            "structure": {
                "high_rpm":{
                    "1X_score": 20,
                    "sine_wave": 20,
                    "1X/Overall": 20,
                    "Amplitude_ISO_Vel_rms": 15,
                    "Amplitude_Similar_Vel_rms": 10,
                    "Direction_Sequence_Vel_rms_structure": 10,
                    "Direction_Sequence_1X_structure": 10,
                    "Angle_Vel_rms_structure": 20,
                    "Angle_1X_structure": 20,
                    "Trend_Vel_rms_structure": 10,
                    "Trend_1X_structure": 10,
                    "Constant_Slope_Vel_rms_structure": 15,
                    "Constant_Slope_1X_structure": 15,
                    "Focus_Vel_rms_structure": 10,
                    "Focus_1X_structure": 10
                },
                "mid_rpm":{
                    "1X_score": 20,
                    "sine_wave": 20,
                    "1X/Overall": 20,
                    "Amplitude_ISO_Vel_rms": 2,
                    "Amplitude_Similar_Vel_rms": 10,
                    "Direction_Sequence_Vel_rms_structure": 10,
                    "Direction_Sequence_1X_structure": 10,
                    "Angle_Vel_rms_structure": 20,
                    "Angle_1X_structure": 20,
                    "Trend_Vel_rms_structure": 10,
                    "Trend_1X_structure": 20,
                    "Constant_Slope_Vel_rms_structure": 15,
                    "Constant_Slope_1X_structure": 15,
                    "Focus_Vel_rms_structure": 10,
                    "Focus_1X_structure": 10
                },
                "low_rpm":{
                    "1X_score": 20,
                    "sine_wave": 20,
                    "1X/Overall": 20,
                    "Amplitude_ISO_Vel_rms": 2,
                    "Amplitude_Similar_Vel_rms": 10,
                    "Direction_Sequence_Vel_rms_structure": 10,
                    "Direction_Sequence_1X_structure": 10,
                    "Angle_Vel_rms_structure": 20,
                    "Angle_1X_structure": 20,
                    "Trend_Vel_rms_structure": 10,
                    "Trend_1X_structure": 20,
                    "Constant_Slope_Vel_rms_structure": 15,
                    "Constant_Slope_1X_structure": 15,
                    "Focus_Vel_rms_structure": 10,
                    "Focus_1X_structure": 10
                }
            },
            "mechanic": {
                "high_rpm": {
                    "1X_score": 10,
                    "2X_score": 20,
                    "3X_score": 20,
                    "4X_score": 20,
                    "5X_score": 20,
                    "harmonic": 20,
                    "1X/Overall": 5,
                    "1X_2X_3X/harmonicas": 15,
                    "3X_4X_5X/harmonicas": 20,
                    "signal_displacement": 15,
                    "Amplitude_ISO_Vel_rms": 5,
                    "Amplitude_ISO_Crest_rms": 10,
                    "Amplitude_Similar_Vel_rms": 15,
                    "Amplitude_Similar_Crest_rms": 15,
                    "Direction_Sequence_Vel_rms_mechanic": 3,
                    "Direction_Sequence_2X_mechanic": 3,
                    "Direction_Sequence_3X_mechanic": 3,
                    "Direction_Sequence_4X_mechanic": 2,
                    "Direction_Sequence_5X_mechanic": 2,
                    "Angle_Vel_rms_mechanic": 2,
                    "Angle_1X_mechanic": 2,
                    "Angle_2X_mechanic": 2,
                    "Angle_3X_mechanic": 2,
                    "Angle_4X_mechanic": 2,
                    "Angle_5X_mechanic": 2,
                    "Trend_Vel_rms_mechanic": 2,
                    "Trend_1X_mechanic": 2,
                    "Trend_2X_mechanic": 2,
                    "Trend_3X_mechanic": 2,
                    "Trend_4X_mechanic": 2,
                    "Trend_5X_mechanic": 2,
                    "Variable_Slope_Vel_rms_mechanic": 2,
                    "Variable_Slope_1X_mechanic": 2,
                    "Variable_Slope_2X_mechanic": 2,
                    "Variable_Slope_3X_mechanic": 2,
                    "Variable_Slope_4X_mechanic": 2,
                    "Variable_Slope_5X_mechanic": 2
                },
                "mid_rpm":{
                    "1X_score": 10, # NOTE: TEST
                    "2X_score": 20,
                    "3X_score": 20,
                    "4X_score": 20,
                    "5X_score": 20,
                    "harmonic": 20,
                    "1X/Overall": 5,
                    "1X_2X_3X/harmonicas": 15,
                    "3X_4X_5X/harmonicas": 20,
                    "signal_displacement": 15,
                    "Amplitude_ISO_Vel_rms": 2,
                    "Amplitude_ISO_Crest_rms": 5,
                    "Amplitude_Similar_Vel_rms": 15,
                    "Amplitude_Similar_Crest_rms": 15,
                    "Direction_Sequence_Vel_rms_mechanic": 0, # NOTE: TEST
                    "Direction_Sequence_2X_mechanic": 3, # NOTE: TEST
                    "Direction_Sequence_3X_mechanic": 3, # NOTE: TEST
                    "Direction_Sequence_4X_mechanic": 2, # NOTE: TEST
                    "Direction_Sequence_5X_mechanic": 2, # NOTE: TEST
                    "Angle_Vel_rms_mechanic": 2,
                    "Angle_1X_mechanic": 2,
                    "Angle_2X_mechanic": 2,
                    "Angle_3X_mechanic": 2,
                    "Angle_4X_mechanic": 2,
                    "Angle_5X_mechanic": 2,
                    "Trend_Vel_rms_mechanic": 10,
                    "Trend_1X_mechanic": 10,
                    "Trend_2X_mechanic": 10,
                    "Trend_3X_mechanic": 10,
                    "Trend_4X_mechanic": 10,
                    "Trend_5X_mechanic": 10,
                    "Variable_Slope_Vel_rms_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_1X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_2X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_3X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_4X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_5X_mechanic": 2 # NOTE: TEST
                },
                "low_rpm":{
                    "1X_score": 10, # NOTE: TEST
                    "2X_score": 20,
                    "3X_score": 20,
                    "4X_score": 20,
                    "5X_score": 20,
                    "harmonic": 20,
                    "1X/Overall": 5,
                    "1X_2X_3X/harmonicas": 15,
                    "3X_4X_5X/harmonicas": 20,
                    "signal_displacement": 15,
                    "Amplitude_ISO_Vel_rms": 2,
                    "Amplitude_ISO_Crest_rms": 5,
                    "Amplitude_Similar_Vel_rms": 15,
                    "Amplitude_Similar_Crest_rms": 15,
                    "Direction_Sequence_Vel_rms_mechanic": 0, # NOTE: TEST
                    "Direction_Sequence_2X_mechanic": 3, # NOTE: TEST
                    "Direction_Sequence_3X_mechanic": 3, # NOTE: TEST
                    "Direction_Sequence_4X_mechanic": 2, # NOTE: TEST
                    "Direction_Sequence_5X_mechanic": 2, # NOTE: TEST
                    "Angle_Vel_rms_mechanic": 2,
                    "Angle_1X_mechanic": 2,
                    "Angle_2X_mechanic": 2,
                    "Angle_3X_mechanic": 2,
                    "Angle_4X_mechanic": 2,
                    "Angle_5X_mechanic": 2,
                    "Trend_Vel_rms_mechanic": 10,
                    "Trend_1X_mechanic": 10,
                    "Trend_2X_mechanic": 10,
                    "Trend_3X_mechanic": 10,
                    "Trend_4X_mechanic": 10,
                    "Trend_5X_mechanic": 10,
                    "Variable_Slope_Vel_rms_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_1X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_2X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_3X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_4X_mechanic": 2, # NOTE: TEST
                    "Variable_Slope_5X_mechanic": 2 # NOTE: TEST
                }
            }
        },
        "Misalignment": {
            "high_rpm": {
                "1X_score": 10,
                "2X_score": 20,
                "3X_score": 10,
                "sine_wave": 10,
                "1X_2X_3X/harmonicas": 10,
                "MW": 20,
                "Amplitude_ISO_Vel_rms": 5,
                "Amplitude_ISO_Crest_rms": 0,
                "Amplitude_Similar_Vel_rms": 0,
                "Amplitude_Similar_Crest_rms": 0,
                "Direction_Sequence_Vel_rms": 10,
                "Direction_Sequence_1X": 10,
                "Direction_Sequence_2X": 20,
                "Direction_Sequence_3X": 10,
                "Direction_Ratio_Vel_rms": 10,
                "Direction_Ratio_1X": 10,
                "Direction_Ratio_2X": 20,
                "Direction_Ratio_3X": 10,
                "Angle_Vel_rms": 0,
                "Angle_1X": 0,
                "Angle_2X": 0,
                "Angle_3X": 0,
                "Trend_Vel_rms": 0,
                "Trend_1X": 0,
                "Trend_2X": 0,
                "Trend_3X": 0,
                "Constant_Slope_Vel_rms": 0,
                "Constant_Slope_1X": 0,
                "Constant_Slope_2X": 0,
                "Constant_Slope_3X": 0,
                "Focus_Vel_rms": 10,
                "Focus_1X": 10,
                "Focus_2X": 20,
                "Focus_3X": 20
            },
            "mid_rpm": {
                "1X_score": 20,
                "2X_score": 20,
                "3X_score": 10,
                "sine_wave": 20,
                "1X_2X_3X/harmonicas": 10,
                "MW": 10,
                "Amplitude_ISO_Vel_rms": 2,
                "Amplitude_ISO_Crest_rms": 0,
                "Amplitude_Similar_Vel_rms": 5,
                "Amplitude_Similar_Crest_rms": 0,
                "Direction_Sequence_Vel_rms": 0,
                "Direction_Sequence_1X": 5, # NOTE: TEST
                "Direction_Sequence_2X": 10, # NOTE: TEST
                "Direction_Sequence_3X": 5, # NOTE: TEST
                "Direction_Ratio_Vel_rms": 10,
                "Direction_Ratio_1X": 10,
                "Direction_Ratio_2X": 20,
                "Direction_Ratio_3X": 10,
                "Angle_Vel_rms": 0,
                "Angle_1X": 0,
                "Angle_2X": 0,
                "Angle_3X": 0,
                "Trend_Vel_rms": 0,
                "Trend_1X": 0,
                "Trend_2X": 0,
                "Trend_3X": 0,
                "Constant_Slope_Vel_rms": 0,
                "Constant_Slope_1X": 0,
                "Constant_Slope_2X": 0,
                "Constant_Slope_3X": 0,
                "Focus_Vel_rms": 10,
                "Focus_1X": 10,
                "Focus_2X": 20,
                "Focus_3X": 20
            },
            "low_rpm": {
                "1X_score": 10,
                "2X_score": 20,
                "3X_score": 10,
                "sine_wave": 10,
                "1X_2X_3X/harmonicas": 10,
                "MW": 20,
                "Amplitude_ISO_Vel_rms": 5,
                "Amplitude_ISO_Crest_rms": 0,
                "Amplitude_Similar_Vel_rms": 0,
                "Amplitude_Similar_Crest_rms": 0,
                "Direction_Sequence_Vel_rms": 10,
                "Direction_Sequence_1X": 10,
                "Direction_Sequence_2X": 20,
                "Direction_Sequence_3X": 10,
                "Direction_Ratio_Vel_rms": 10,
                "Direction_Ratio_1X": 10,
                "Direction_Ratio_2X": 20,
                "Direction_Ratio_3X": 10,
                "Angle_Vel_rms": 0,
                "Angle_1X": 0,
                "Angle_2X": 0,
                "Angle_3X": 0,
                "Trend_Vel_rms": 0,
                "Trend_1X": 0,
                "Trend_2X": 0,
                "Trend_3X": 0,
                "Constant_Slope_Vel_rms": 0,
                "Constant_Slope_1X": 0,
                "Constant_Slope_2X": 0,
                "Constant_Slope_3X": 0,
                "Focus_Vel_rms": 10,
                "Focus_1X": 10,
                "Focus_2X": 20,
                "Focus_3X": 20
            }
        },
        "Bearing": {
            "high_rpm": {
                "acc_iso": 1,
                "crest_iso": 1,
                "kurt_iso": 1,
                "acc_trend": 1,
                "crest_trend": 1,
                "kurt_trend": 1,
                "hump_score": 1,
                "BPFI_harmonics": 1,
                "BSF_harmonics": 1,
                "BPFO_harmonics": 1,
                "FTF_harmonics": 1,
                "model_prediction": 1,
                "acc_iso": 1,
                "0_48X": 1,
                "looseness_harmonics": 1,
                "0_5X_harmonics": 1
            },
            "mid_rpm": {
                "acc_iso": 1,
                "crest_iso": 1,
                "kurt_iso": 1,
                "acc_trend": 1,
                "crest_trend": 1,
                "kurt_trend": 1,
                "hump_score": 1,
                "BPFI_harmonics": 1,
                "BSF_harmonics": 1,
                "BPFO_harmonics": 1,
                "FTF_harmonics": 1,
                "model_prediction": 1,
                "acc_iso": 1,
                "0_48X": 1,
                "looseness_harmonics": 1,
                "0_5X_harmonics": 1
            },
            "low_rpm": {
                "acc_iso": 1,
                "crest_iso": 1,
                "kurt_iso": 1,
                "acc_trend": 1,
                "crest_trend": 1,
                "kurt_trend": 1,
                "hump_score": 1,
                "BPFI_harmonics": 1,
                "BSF_harmonics": 1,
                "BPFO_harmonics": 1,
                "FTF_harmonics": 1,
                "model_prediction": 1,
                "acc_iso": 1,
                "0_48X": 1,
                "looseness_harmonics": 1,
                "0_5X_harmonics": 1
            },
        },
        "Gearbox": 
        {
            "high_rpm": {
                "vel_iso": 1,
                "crest_iso": 1,
                "kurt_iso": 1,
                "side_band": 1,
                "impulse": 1,
                "vel_trend": 1,
                "crest_trend": 1,
                "side_band_trend": 1,
                "model_prediction": 1,
                "gmf": 1,
                "hump": 1
            },
            "mid_rpm": {
                "vel_iso": 1,
                "crest_iso": 1,
                "kurt_iso": 1,
                "side_band": 1,
                "impulse": 1,
                "vel_trend": 1,
                "crest_trend": 1,
                "side_band_trend": 1,
                "model_prediction": 1,
                "gmf": 1,
                "hump": 1
            },
            "low_rpm": {
                "vel_iso": 1,
                "crest_iso": 1,
                "kurt_iso": 1,
                "side_band": 1,
                "impulse": 1,
                "vel_trend": 1,
                "crest_trend": 1,
                "side_band_trend": 1,
                "model_prediction": 1,
                "gmf": 1,
                "hump": 1
            },
        }
    }
}

# ============================================================================================================================================
# Input Section ================================================================================================
# failures = ['Unbalance', 'Looseness', 'Misalignment', 'Coupling', 'Bearing', 'Gearbox'] # List of failure we can detected so far
#============================== correct data ===============================

fan_type = {'1112IM1':'center_hung',
            '1112IM3':'center_hung',
            # ===================
            '000CP001':'over_hung',
            '2511ND1':'over_hung',
            '3090-1001':'over_hung',
            'F-200':'over_hung',
            'P-3001WC2' : 'over_hung',
            '2030-3001' : 'over_hung',
            '532FN502' : 'over_hung',
            '123CF014' : 'over_hung',
            '423FN1' : 'over_hung',
            '441FN300' : 'over_hung',
            '441FN305' : 'over_hung',
            '331FN400' : 'over_hung',
            '531FN380' : 'over_hung',
            '531MS140' : 'over_hung',
            'M-100' : 'over_hung',
            # ===================
            '331.FN110' : 'center_hung',
            '431.FN560' : 'over_hung',
            #====================
            '04EPU' : 'over_hung',
            '05EPU' : 'over_hung',
            '06EPU' : 'over_hung',
            '07EPU' : 'over_hung',
            '08EPU' : 'over_hung',
            '09EPU' : 'over_hung',
            '10EPU' : 'over_hung',
            '11EPU' : 'over_hung',
            #====================
            'CP-BA48' : 'over_hung',
            # ===================
            '2513SR1':'over_hung',
            '2511RM1':'over_hung',
            '2513FN1':'center_hung',
            '2511SR1':'over_hung',
            '2403': 'over_hung',
            '3703': 'over_hung',
            'A-002': 'over_hung',
            '3111FN1': 'center_hung',
            '3511MD1': 'over_hung',
            '3511KL1': 'over_hung',
            '3612CR1': 'center_hung',
            '3611FN0': 'over_hung',
            '3611FN1': 'over_hung',
            '3611FN2': 'over_hung',
            '3611FN3': 'over_hung',
            '3611FN4': 'over_hung',
            '3611FN5': 'over_hung',
            '3611FN6': 'over_hung',
            '3611FN7': 'over_hung',
            '3218FN1': 'center_hung',
            '3618FN1': 'center_hung',
            '5411BM1': 'center_hung',
            '5421BM1': 'center_hung',
            '5411SR1': 'center_hung',
            '5421SR1': 'center_hung',
            '5413SR1': 'center_hung',
            '5423SR1': 'center_hung',
            '5413FN1': 'over_hung',
            '501-RJ': 'center_hung',
            '5423FN1': 'over_hung',
            #=======================
            '2516BL1' : 'center_hung',
            '2516BL2' : 'center_hung',
            '2516BL3' : 'center_hung',
            '2816BL1' : 'center_hung',
            '2816BL2' : 'center_hung',
            '2816BL3' : 'center_hung',
            '7411CP1' : 'center_hung',
            '7411CP2' : 'center_hung',
            '7411CP3' : 'center_hung',
            '7411CP4' : 'center_hung',
            '7411CP5' : 'center_hung',
            '7412CP1' : 'center_hung',
            '7412CP2' : 'center_hung',
            '7412CP3' : 'center_hung',
            '7412CP4' : 'center_hung'}

power = {'1112IM1':'group_1',
         '1112IM3':'group_1',
         '2513SR1':'group_2',
         #=================================
         'CP-BA48':'group_1',
         'M-100' : 'group_2',
        # ===================
        '331.FN110' : 'group_1',
        '431.FN560' : 'group_2',
         #=================================
        '04EPU' : 'group_2',
        '05EPU' : 'group_2',
        '06EPU' : 'group_2',
        '07EPU' : 'group_2',
        '08EPU' : 'group_2',
        '09EPU' : 'group_2',
        '10EPU' : 'group_2',
        '11EPU' : 'group_2',
        #====================
         '2511RM1':'group_1',
         '2513FN1':'group_1',
         '2511SR1':'group_2',
         '3111FN1': 'group_1',
         '2403': 'group_1',
         'A-002': 'group_1',
         '3511MD1': 'group_1',
         '3612CR1': 'group_2',
         '3703': 'group_2',
         '3611FN0': 'group_2',
         '3611FN1': 'group_2',
         '3611FN2': 'group_2',
         '3611FN3': 'group_2',
         '3611FN4': 'group_2',
         '3611FN5': 'group_2',
         '3611FN6': 'group_2',
         '3611FN7': 'group_2',
         '3218FN1': 'group_1',
         '3618FN1': 'group_1',
         '5411BM1': 'group_1',
         '5421BM1': 'group_1',
         '5411SR1': 'group_2',
         '5413SR1': 'group_2',
         '5421SR1': 'group_2',
         '5423SR1': 'group_2',
         '5413FN1': 'group_1',
         '501-RJ': 'group_2',
         '5423FN1': 'group_1',
         #=======================
        '2516BL1' : 'group_2',
        '2516BL2' : 'group_2',
        '2516BL3' : 'group_2',
        '2816BL1' : 'group_2',
        '2816BL2' : 'group_2',
        '2816BL3' : 'group_2',
        '7411CP1' : 'group_2',
        '7411CP2' : 'group_2',
        '7411CP3' : 'group_2',
        '7411CP4' : 'group_2',
        '7411CP5' : 'group_2',
        '7412CP1' : 'group_2',
        '7412CP2' : 'group_2',
        '7412CP3' : 'group_2',
        '7412CP4' : 'group_2'}

foundation = {'1112IM1':'rigid',
            '1112IM3':'rigid',
            '2513SR1':'rigid',
            '2511RM1':'rigid',
            '2513FN1':'rigid',
            '2511SR1':'rigid',
            '3111FN1': 'rigid',
            '2403': 'rigid',
            'A-002': 'rigid',
            'M-100' : 'rigid',
            #=================================
            'CP-BA48': 'rigid',
            # ===================
            '331.FN110' : 'rigid',
            '431.FN560' : 'flexible',
            #=================================
            '04EPU' : 'rigid',
            '05EPU' : 'rigid',
            '06EPU' : 'rigid',
            '07EPU' : 'rigid',
            '08EPU' : 'rigid',
            '09EPU' : 'rigid',
            '10EPU' : 'rigid',
            '11EPU' : 'rigid',
            #====================
            '3511MD1': 'rigid',
            '3612CR1': 'rigid',
            '3611FN0': 'flexible',
            '3703': 'flexible',
            '3611FN1': 'flexible',
            '3611FN2': 'flexible',
            '3611FN3': 'flexible',
            '3611FN4': 'flexible',
            '3611FN5': 'flexible',
            '3611FN6': 'flexible',
            '3611FN7': 'flexible',
            '3218FN1': 'rigid',
            '3618FN1': 'rigid',
            '5411BM1': 'rigid',
            '5421BM1': 'rigid',
            '5411SR1': 'rigid',
            '5413SR1': 'rigid',
            '5421SR1': 'rigid',
            '5423SR1': 'rigid',
            '5413FN1': 'flexible',
            '501-RJ': 'rigid',
            '5423FN1': 'flexible',
            #=======================
            '2516BL1' : 'flexible',
            '2516BL2' : 'flexible',
            '2516BL3' : 'flexible',
            '2816BL1' : 'flexible',
            '2816BL2' : 'flexible',
            '2816BL3' : 'flexible',
            '7411CP1' : 'flexible',
            '7411CP2' : 'flexible',
            '7411CP3' : 'flexible',
            '7411CP4' : 'flexible',
            '7411CP5' : 'flexible',
            '7412CP1' : 'flexible',
            '7412CP2' : 'flexible',
            '7412CP3' : 'flexible',
            '7412CP4' : 'flexible'}

rpm = {#======================================================
       'CP-BA48' : {'1' : {"reference": "Fix","value": 1490},
                    '2' : {"reference": "Fix","value": 1490},
                    '3' : {"reference": "Fix","value": 1490},
                    '4' : {"reference": "Fix","value": 1490},
                    '5' : {"reference": "Fix","value": 429},
                    '6' : {"reference": "Fix","value": 429},
                    '7' : {"reference": "Fix","value": 429},
                    '8' : {"reference": "Fix","value": 429},
                    '9' : {"reference": "Fix","value": 429},
                    '10' : {"reference": "Fix","value": 429}}, 
       #======================================================
        '04EPU' : {'1' : {"reference": "Fix","value": 1453},
                  '2' : {"reference": "Fix","value": 1453},
                  '3' : {"reference": "Fix","value": 1453},
                  '4' : {"reference": "Fix","value": 1453}},
        #======================================================
        '3703' : {'1' : {"reference": "Fix","value": 1490},
                  '2' : {"reference": "Fix","value": 1490},
                  '3' : {"reference": "Fix","value": 2512},
                  '4' : {"reference": "Fix","value": 2512}},
        #======================================================
        '05EPU' :  {'1' : {"reference": "Fix","value": 2990},
                  '2' : {"reference": "Fix","value": 2990},
                  '3' : {"reference": "Fix","value": 2990},
                  '4' : {"reference": "Fix","value": 2990}},
        #======================================================
        '06EPU' :  {'1' : {"reference": "Fix","value": 1443},
                  '2' : {"reference": "Fix","value": 1443},
                  '3' : {"reference": "Fix","value": 1443},
                  '4' : {"reference": "Fix","value": 1443}},
        #======================================================
        '07EPU' : {'1' : {"reference": "Fix","value": 1443},
                  '2' : {"reference": "Fix","value": 1443},
                  '3' : {"reference": "Fix","value": 1443},
                  '4' : {"reference": "Fix","value": 1443}},
        #======================================================
        '08EPU' : {'1' : {"reference": "Fix","value": 1453},
                  '2' : {"reference": "Fix","value": 1453},
                  '3' : {"reference": "Fix","value": 1453},
                  '4' : {"reference": "Fix","value": 1453}},
        #======================================================
        '09EPU' : {'1' : {"reference": "Fix","value": 1453},
                  '2' : {"reference": "Fix","value": 1453},
                  '3' : {"reference": "Fix","value": 1453},
                  '4' : {"reference": "Fix","value": 1453}},
        #======================================================
        '10EPU' : {'1' : {"reference": "Fix","value": 2971},
                  '2' : {"reference": "Fix","value": 2971},
                  '3' : {"reference": "Fix","value": 2971},
                  '4' : {"reference": "Fix","value": 2971}},
        #======================================================
        '11EPU' : {'1' : {"reference": "Fix","value": 2971},
                  '2' : {"reference": "Fix","value": 2971},
                  '3' : {"reference": "Fix","value": 2971},
                  '4' : {"reference": "Fix","value": 2971}},
        #======================================================
        '331.FN110' : {'1' : {"reference": "Fix","value": 825},
                       '2' : {"reference": "Fix","value": 825},
                       '3' : {"reference": "Fix","value": 825},
                       '4' : {"reference": "Fix","value": 825}},
        #======================================================
        '431.FN560' : {'1' : {"reference": "Fix","value": 1218},
                       '2' : {"reference": "Fix","value": 1218},
                       '3' : {"reference": "Fix","value": 1218},
                       '4' : {"reference": "Fix","value": 1218}},
        #======================================================
        '1112IM1' : {'1' : {"reference": "Fix","value": 990},
                     '2' :{"reference": "Fix","value": 990},
                     '3' :{"reference": "Fix","value": 990},
                     '4' :{"reference": "Fix","value": 990},
                     '5' : {"reference": "Fix","value": 360},
                     '6' : {"reference": "Fix","value": 360}},
        #======================================================
        '1112IM3' : {'1' : {"reference": "Fix","value": 990},
                     '2' :{"reference": "Fix","value": 990},
                     '3' :{"reference": "Fix","value": 990},
                     '4' :{"reference": "Fix","value": 990},
                     '5' : {"reference": "Fix","value": 360},
                     '6' : {"reference": "Fix","value": 360}},
        #======================================================
        '2513SR1': {'1' : {"reference": "Fix","value": 1240},
                     '2' :{"reference": "Fix","value": 1240},
                     '3' :{"reference": "Fix","value": 1240},
                     '4' :{"reference": "Fix","value": 1240},
                     '5' : {"reference": "Fix","value":300},
                     '6' : {"reference": "Fix","value":300},
                     '7' : {"reference": "Fix","value":150},
                     '8' : {"reference": "Fix","value":150},
                     '9' : {"reference": "Fix","value":70},
                     '10':{"reference": "Fix","value":70},
                     '11':{"reference": "Fix","value":70}},
        #======================================================
        '2511RM1': {'1' : {"reference": "Fix","value": 990},
                    '2' : {"reference": "Fix","value": 990},
                    '3' : {"reference": "Fix","value": 990},
                    '4' : {"reference": "Fix","value": 990},
                    '5' : {"reference": "Fix","value": 127},
                    '6' : {"reference": "Fix","value": 127},
                    '7' : {"reference": "Fix","value": 470},
                    '8' : {"reference": "Fix","value": 24}},
        #====================================================== 
        '2513FN1': {'1' : {"reference": "Fix","value": 994},
                    '2' : {"reference": "Fix","value": 994},
                    '3' : {"reference": "Fix","value": 994},
                    '4' : {"reference": "Fix","value": 994}},
        #======================================================
        '2511SR1': {'1' : {"reference": "Fix","value": 1240},
                     '2' :{"reference": "Fix","value": 1240},
                     '3' :{"reference": "Fix","value": 1240},
                     '4' :{"reference": "Fix","value": 1240},
                     '5' : {"reference": "Fix","value":300},
                     '6' : {"reference": "Fix","value":300},
                     '7' : {"reference": "Fix","value":150},
                     '8' : {"reference": "Fix","value":150},
                     '9' : {"reference": "Fix","value":70},
                     '10':{"reference": "Fix","value":70}},
        #======================================================
        '3111FN1': {'1' : {"reference": "Fix","value": 850},
                    '2' : {"reference": "Fix","value": 850},
                    '3' : {"reference": "Fix","value": 850},
                    '4' : {"reference": "Fix","value": 850}},
        #======================================================
        '2403'   : {'1' : {"reference": "Fix","value": 800},
                    '2' : {"reference": "Fix","value": 800},
                    '3' : {"reference": "Fix","value": 800},
                    '4' : {"reference": "Fix","value": 800}},
        #====================================================== 
        'A-002'  : {'1' : {"reference": "Fix","value": 1453},
                    '2' : {"reference": "Fix","value": 1453},
                    '3' : {"reference": "Fix","value": 1453},
                    '4' : {"reference": "Fix","value": 1453},
                    '5' : {"reference": "Fix","value": 497},
                    '6' : {"reference": "Fix","value": 497},
                    '7' : {"reference": "Fix","value": 500},
                    '8' : {"reference": "Fix","value": 500},
                    '9' : {"reference": "Fix","value": 500},
                    '10' : {"reference": "Fix","value": 500},
                    '11' : {"reference": "Fix","value": 500},
                    '12' : {"reference": "Fix","value": 500}},
        #======================================================
        '3511MD1': {'1' : {"reference": "Fix","value": 1429},
                    '2' : {"reference": "Fix","value": 1429},
                    '3' : {"reference": "Fix","value": 1429},
                    '4' : {"reference": "Fix","value": 1429},
                    '5' : {"reference": "Fix","value": 330},
                    '6' : {"reference": "Fix","value": 330},
                    '7' : {"reference": "Fix","value": 83},
                    '8' : {"reference": "Fix","value": 83},
                    '9' : {"reference": "Fix","value": 21.12},
                    '10' : {"reference": "Fix","value":21.12},
                    '11' : {"reference": "Fix","value":21.12},
                    '12' : {"reference": "Fix","value":21.12}},
        #======================================================
        '3612CR1': {'1' : {"reference": "Fix","value": 993},
                    '2' : {"reference": "Fix","value": 993},
                    '3' : {"reference": "Fix","value": 367},
                    '4' : {"reference": "Fix","value": 367}},
        #======================================================
        '3611FN0': {'1' : {"reference": "Fix","value": 1500},
                    '2' : {"reference": "Fix","value": 1500},
                    '3' : {"reference": "Fix","value": 1500},
                    '4' : {"reference": "Fix","value": 1500}},
        #======================================================
        '3611FN1': {'1' : {"reference": "Fix","value": 1500},
                    '2' : {"reference": "Fix","value": 1500},
                    '3' : {"reference": "Fix","value": 1500},
                    '4' : {"reference": "Fix","value": 1500}},
        #======================================================
        '3611FN2': {'1' : {"reference": "Fix","value": 1490},
                    '2' : {"reference": "Fix","value": 1490},
                    '3' : {"reference": "Fix","value": 1285},
                    '4' : {"reference": "Fix","value": 1285}},
        #======================================================
        '3611FN3': {'1' : {"reference": "Fix","value": 1490},
                    '2' : {"reference": "Fix","value": 1490},
                    '3' : {"reference": "Fix","value": 1406},
                    '4' : {"reference": "Fix","value": 1406}},
        #======================================================
        '3611FN4': {'1' : {"reference": "Fix","value": 1490},
                    '2' : {"reference": "Fix","value": 1490},
                    '3' : {"reference": "Fix","value": 1406},
                    '4' : {"reference": "Fix","value": 1406}},
        #======================================================
        '3611FN5': {'1' : {"reference": "Fix","value": 1490},
                    '2' : {"reference": "Fix","value": 1490},
                    '3' : {"reference": "Fix","value": 1406},
                    '4' : {"reference": "Fix","value": 1406}}, 
        #======================================================
        '3611FN6': {'1' : {"reference": "Fix","value": 1500},
                    '2' : {"reference": "Fix","value": 1500},
                    '3' : {"reference": "Fix","value": 1500},
                    '4' : {"reference": "Fix","value": 1500}},
        #======================================================
        '3611FN7': {'1' : {"reference": "Fix","value": 1490},
                    '2' : {"reference": "Fix","value": 1490},
                    '3' : {"reference": "Fix","value": 1290},
                    '4' : {"reference": "Fix","value": 1290}},
        #======================================================
        '3218FN1': {'1' : {"reference": "Fix","value": 780},
                    '2' : {"reference": "Fix","value": 780},
                    '3' : {"reference": "Fix","value": 780},
                    '4' : {"reference": "Fix","value": 780},
                    '5' : {"reference": "Fix","value": 420},
                    '6' : {"reference": "Fix","value": 420},
                    '7' : {"reference": "Fix","value": 420},
                    '8' : {"reference": "Fix","value": 420}},
        #======================================================
        '3618FN1': {'1' : {"reference": "Fix","value": 468},
                    '2' : {"reference": "Fix","value": 468},
                    '3' : {"reference": "Fix","value": 468},
                    '4' : {"reference": "Fix","value": 468}},
        #======================================================
        '5411BM1': {'1' : {"reference": "Fix","value": 990},
                    '2' : {"reference": "Fix","value": 990},
                    '3' : {"reference": "Fix","value": 990},
                    '4' : {"reference": "Fix","value": 250},
                    '5' : {"reference": "Fix","value": 15},
                    '6' : {"reference": "Fix","value": 15}},
        #======================================================
        '5421BM1': {'1' : {"reference": "Fix","value": 990},
                    '2' :{"reference": "Fix","value": 990},
                    '3' :{"reference": "Fix","value": 990},
                    '4' :{"reference": "Fix","value": 250},
                    '5' : {"reference": "Fix","value": 15},
                    '6' : {"reference": "Fix","value": 15}}, 
        #======================================================
        '5411SR1': {'1' : {"reference": "Fix","value": 1200},
                    '2' : {"reference": "Fix","value": 1200},
                    '3' : {"reference": "Fix","value": 1200},
                    '4' : {"reference": "Fix","value": 1200},
                    '5' : {"reference": "Fix","value": 500},
                    '6' : {"reference": "Fix","value": 500},
                    '7' : {"reference": "Fix","value": 200},
                    '8' : {"reference": "Fix","value": 200}},
        #======================================================
        '5413SR1': {'1' : {"reference": "Fix","value": 1170},
                    '2' : {"reference": "Fix","value": 1170},
                    '3' : {"reference": "Fix","value": 1170},
                    '4' : {"reference": "Fix","value": 1170},
                    '5' : {"reference": "Fix","value": 500},
                    '6' : {"reference": "Fix","value": 500},
                    '7' : {"reference": "Fix","value": 167},
                    '8' : {"reference": "Fix","value": 167},
                    '9' : {"reference": "Fix","value": 167}},
        #======================================================
        '5421SR1': {'1' : {"reference": "Fix","value": 1200},
                    '2' : {"reference": "Fix","value": 1200},
                    '3' : {"reference": "Fix","value": 1200},
                    '4' : {"reference": "Fix","value": 1200},
                    '5' : {"reference": "Fix","value": 500},
                    '6' : {"reference": "Fix","value": 500},
                    '7' : {"reference": "Fix","value": 200},
                    '8' : {"reference": "Fix","value": 200}},
        #======================================================
        '5423SR1': {'1' : {"reference": "Fix","value": 1170},
                    '2' : {"reference": "Fix","value": 1170},
                    '3' : {"reference": "Fix","value": 1170},
                    '4' : {"reference": "Fix","value": 1170},
                    '5' : {"reference": "Fix","value": 500},
                    '6' : {"reference": "Fix","value": 500},
                    '7' : {"reference": "Fix","value": 167},
                    '8' : {"reference": "Fix","value": 167},
                    '9' : {"reference": "Fix","value": 167}},
        #======================================================
        '5413FN1': {'1' : {"reference": "Fix","value": 990},
                    '2' : {"reference": "Fix","value": 990},
                    '3' : {"reference": "Fix","value": 990},
                    '4' : {"reference": "Fix","value": 990}},
        #======================================================
        'M-100': {'1' : {"reference": "Fix","value": 1480},
                  '2' : {"reference": "Fix","value": 1480},
                  '3' : {"reference": "Fix","value": 1480},
                  '4' : {"reference": "Fix","value": 1480}},
        #====================================================== 
        '5423FN1': {'1' : {"reference": "Fix","value": 990},
                    '2' : {"reference": "Fix","value": 990},
                    '3' : {"reference": "Fix","value": 990},
                    '4' : {"reference": "Fix","value": 990}},
        #======================================================
        '501-RJ': {'1' : {"reference": "Fix","value": 1453},
                    '2' : {"reference": "Fix","value": 1453},
                    '3' : {"reference": "Fix","value": 290},
                    '4' : {"reference": "Fix","value": 290},
                    '5' : {"reference": "Fix","value": 290},
                    '6' : {"reference": "Fix","value": 290},
                    '7' : {"reference": "Fix","value": 290},
                    '8' : {"reference": "Fix","value": 290},
                    '9' : {"reference": "Fix","value": 290},
                    '10' : {"reference": "Fix","value": 290}},
        #======================================================
        '2516BL1': {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1887},
                '4' : {"reference": "Fix","value": 1887},
                '5' : {"reference": "Fix","value": 1887},
                '6' : {"reference": "Fix","value": 1887}},
        #======================================================
        '2516BL2':{'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1887},
                '4' : {"reference": "Fix","value": 1887},
                '5' : {"reference": "Fix","value": 1887},
                '6' : {"reference": "Fix","value": 1887}},
        #======================================================
        '2516BL3':{'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1887},
                '4' : {"reference": "Fix","value": 1887},
                '5' : {"reference": "Fix","value": 1887},
                '6' : {"reference": "Fix","value": 1887}},
        #======================================================
        '2816BL1': {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1887},
                '4' : {"reference": "Fix","value": 1887},
                '5' : {"reference": "Fix","value": 1887},
                '6' : {"reference": "Fix","value": 1887}},
        #======================================================
        '2816BL2':{'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1887},
                '4' : {"reference": "Fix","value": 1887},
                '5' : {"reference": "Fix","value": 1887},
                '6' : {"reference": "Fix","value": 1887}},
        #======================================================
        '2816BL3': {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1887},
                '4' : {"reference": "Fix","value": 1887},
                '5' : {"reference": "Fix","value": 1887},
                '6' : {"reference": "Fix","value": 1887}},
        #======================================================
        '7411CP1': {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7411CP2':  {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7411CP3':  {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7411CP4': {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7411CP5':  {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7412CP1':  {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7412CP2':  {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7412CP3': {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        '7412CP4': {'1' : {"reference": "Fix","value": 1490},
                '2' : {"reference": "Fix","value": 1490},
                '3' : {"reference": "Fix","value": 1490},
                '4' : {"reference": "Fix","value": 1490},
                '5' : {"reference": "Fix","value": 1556},
                '6' : {"reference": "Fix","value": 1556},
                '7' : {"reference": "Fix","value": 1037},
                '8' : {"reference": "Fix","value": 1037}},
        #======================================================
        }

# Group subgroup equipment ==============================================================================================
equipments_typ = {'112RM044': ['Roller Mill', 'Mill'],
 '2511MD1': ['Roller Mill', 'Mill'],
 '2511RM1': ['Roller Mill', 'Mill'],
 '341-RM': ['Roller Mill', 'Mill'],
 '342-RM': ['Roller Mill', 'Mill'],
 'A-100': ['Roller Mill', 'Mill'],
 'R-102': ['Roller Mill', 'Mill'],
#=================================
'04EPU' : ['ID Fan', 'Fan'],
'05EPU' : ['ID Fan', 'Fan'],
'06EPU' : ['ID Fan', 'Fan'],
'07EPU' : ['ID Fan', 'Fan'],
'08EPU' : ['ID Fan', 'Fan'],
'09EPU' : ['ID Fan', 'Fan'],
'10EPU' : ['ID Fan', 'Fan'],
'11EPU' : ['ID Fan', 'Fan'],
#====================
'331.FN110' : ['ID Fan', 'Fan'],
'431.FN560' : ['Cooler Fan', 'Fan'],
#====================
 '2511-RM01': ['Roller Mill', 'Mill'],
 '113MF01': ['Mill Fan', 'Fan'],
 '341-MF': ['Mill Fan', 'Fan'],
 '2513FN1': ['Mill Fan', 'Fan'],
 'F-200': ['Mill Fan', 'Fan'],
 '121ID01': ['ID Fan', 'Fan'],
 '450-FN': ['ID Fan', 'Fan'],
 '3111FN1': ['ID Fan', 'Fan'],
 '2403': ['ID Fan', 'Fan'],
 'F-100': ['ID Fan', 'Fan'],
 '122RK000': ['Kiln', 'Kiln'],
 '431-KL': ['Kiln', 'Kiln'],
 '3511MD1': ['Kiln', 'Kiln'],
 'K-100': ['Kiln', 'Kiln'],
 '125BELT': ['Belt Conveyor', 'Conveyor'],
 '146BELT': ['Belt Conveyor', 'Conveyor'],
 '275BELT': ['Belt Conveyor', 'Conveyor'],
 '283BELT': ['Belt Conveyor', 'Conveyor'],
 'AMUND-MAIN': ['Belt Conveyor', 'Conveyor'],
 'AMUND-RIJK': ['Belt Conveyor', 'Conveyor'],
 '010-BC': ['Belt Conveyor', 'Conveyor'],
 '020-BC': ['Belt Conveyor', 'Conveyor'],
 '130-BC': ['Belt Conveyor', 'Conveyor'],
 '221-BC': ['Belt Conveyor', 'Conveyor'],
 '511-BC': ['Belt Conveyor', 'Conveyor'],
 '1115BC2': ['Belt Conveyor', 'Conveyor'],
 '132BM01': ['Ball Mill', 'Mill'],
 'A-002': ['Ball Mill', 'Mill'],
 '133BM01': ['Ball Mill', 'Mill'],
 '232BM02': ['Ball Mill', 'Mill'],
 '233BM02': ['Ball Mill', 'Mill'],
 '531-BM': ['Ball Mill', 'Mill'],
 '532-BM': ['Ball Mill', 'Mill'],
 '5411BM1': ['Ball Mill', 'Mill'],
 '5421BM1': ['Ball Mill', 'Mill'],
 'A-300': ['Ball Mill', 'Mill'],
 'A-400': ['Ball Mill', 'Mill'],
 '5411MD1': ['Ball Mill', 'Mill'],
 'AMUND-CEME': ['inlet feed', 'Conveyor'],
 '111-AP': ['Apron', 'Conveyor'],
 '111-CR': ['Crusher', 'Crusher'],
 '361-CR': ['Crusher', 'Crusher'],
 '1112IM1': ['Crusher', 'Crusher'],
 '1112IM3': ['Crusher', 'Crusher'],
 '3612CR1': ['Crusher', 'Crusher'],
 'C-100': ['Crusher', 'Crusher'],
 'C-300': ['Crusher', 'Crusher'],
 '210-RC': ['Chain Conveyor', 'Conveyor'],
 '341-SR': ['Separator', 'Separator'],
 '531-SR': ['Separator', 'Separator'],
 '532-SR': ['Separator', 'Separator'],
 '2511SR1': ['Separator', 'Separator'],
 '2513SR1': ['Separator', 'Separator'],
 '5413SR1': ['Separator', 'Separator'],
 '5421SR1': ['Separator', 'Separator'],
 '5423SR1': ['Separator', 'Separator'],
 '361-FN': ['EP Fan - ESP Fan', 'Fan'],
 '461-FN': ['EP Fan - ESP Fan', 'Fan'],
 '3218FN1': ['EP Fan - ESP Fan', 'Fan'],
 '3618FN1': ['EP Fan - ESP Fan', 'Fan'],
 'F-300': ['EP Fan - ESP Fan', 'Fan'],
 '412-EL': ['Elevator', 'Conveyor'],
 '5415BE1': ['Elevator', 'Conveyor'],
 '441-FN': ['Cooler Fan', 'Fan'],
 '3703': ['Cooler Fan', 'Fan'],
 '3611FN0': ['Cooler Fan', 'Fan'],
 '3611FN1': ['Cooler Fan', 'Fan'],
 '3611FN2': ['Cooler Fan', 'Fan'],
 '3611FN3': ['Cooler Fan', 'Fan'],
 '3611FN4': ['Cooler Fan', 'Fan'],
 '3611FN5': ['Cooler Fan', 'Fan'],
 '3611FN6': ['Cooler Fan', 'Fan'],
 '3611FN7': ['Cooler Fan', 'Fan'],
 'M-100': ['Cooler Fan', 'Fan'],
 '501-RJ': ['Pan Conveyor', 'Conveyor'],
 '501-SI': ['Pan Conveyor', 'Conveyor'],
 '531-FN': ['BF Fan - Bin Fan - Siloo', 'Fan'],
 '532-FN': ['BF Fan - Bin Fan - Siloo', 'Fan'],
 '5413FN1': ['BF Fan - Bin Fan - Siloo', 'Fan'],
 '5423FN1': ['BF Fan - Bin Fan - Siloo', 'Fan'],
 'F-400': ['BF Fan - Bin Fan - Siloo', 'Fan'],
 '2816BL1': ['Blower', 'Conveyor'],
 '2816BL3': ['Blower', 'Conveyor'],
 '501-RJ': ['Belt Conveyor', 'Conveyor'],
 #=================================
 'CP-BA48': ['Blower', 'Conveyor'],
 #=======================
'2516BL1' : ['Blower', 'Conveyor'],
'2516BL2' : ['Blower', 'Conveyor'],
'2516BL3' : ['Blower', 'Conveyor'],
'2816BL1' : ['Blower', 'Conveyor'],
'2816BL2' : ['Blower', 'Conveyor'],
'2816BL3' : ['Blower', 'Conveyor'],
# '7411CP1' : ['Compressor', 'Compressor'],
# '7411CP2' : ['Compressor', 'Compressor'],
# '7411CP3' : ['Compressor', 'Compressor'],
# '7411CP4' : ['Compressor', 'Compressor'],
# '7411CP5' : ['Compressor', 'Compressor'],
# '7412CP1' : ['Compressor', 'Compressor'],
# '7412CP2' : ['Compressor', 'Compressor'],
# '7412CP3' : ['Compressor', 'Compressor'],
# '7412CP4' : ['Compressor', 'Compressor'],
'7411CP1' : ['Blower', 'Conveyor'],
'7411CP2' : ['Blower', 'Conveyor'],
'7411CP3' : ['Blower', 'Conveyor'],
'7411CP4' : ['Blower', 'Conveyor'],
'7411CP5' : ['Blower', 'Conveyor'],
'7412CP1' : ['Blower', 'Conveyor'],
'7412CP2' : ['Blower', 'Conveyor'],
'7412CP3' : ['Blower', 'Conveyor'],
'7412CP4' : ['Blower', 'Conveyor'],
#=======================
'000CP001' : ['Blower', 'Conveyor'],
'000CP002' : ['Blower', 'Conveyor'],
'000CP003' : ['Blower', 'Conveyor'],
'000CP004' : ['Blower', 'Conveyor'],
'101CR010' : ['Crusher', 'Crusher'],
'112MF053' : ['Mill Fan', 'Fan'],
'112RM444' : ['Ball Mill', 'Mill'],
'113BL002' : ['Blower', 'Conveyor'],
'113BL003' : ['Blower', 'Conveyor'],
'113BL004' : ['Blower', 'Conveyor'],
'115BL065' : ['Blower', 'Conveyor'],
'115BL066' : ['Blower', 'Conveyor'],
'116EP007' : ['EP Fan - ESP Fan', 'Fan'],
'121ID001' : ['ID Fan', 'Fan'],
'122RK000': ['Kiln', 'Kiln'],
'123CF013' : ['Cooler Fan', 'Fan'],
'123CF014' : ['Cooler Fan', 'Fan'],
'123CF015' : ['Cooler Fan', 'Fan'],
'123CF016' : ['Cooler Fan', 'Fan'],
'123CF017' : ['Cooler Fan', 'Fan'],
'123CF018' : ['Cooler Fan', 'Fan'],
'123CF019' : ['Cooler Fan', 'Fan'],
'124ES012' : ['EP Fan - ESP Fan', 'Fan'],
'132CM014' : ['Ball Mill', 'Mill'],
'132CM024' : ['Ball Mill', 'Mill'],
'133BH004' : ['Mill Fan', 'Fan'],
'133BH024' : ['Mill Fan', 'Fan'],
# ===================================
"01EPU01310300-04" : ['Blower', 'Conveyor'],
"01EPU01310300-13" : ['Blower', 'Conveyor'],
"01EPU01310300-14" : ['Blower', 'Conveyor'],
"01EPU01310300-19" : ['Blower', 'Conveyor'],
"01EPU01310300-15" : ['Blower', 'Conveyor'],
"01EPU01310300-05" : ['Blower', 'Conveyor'],
"01EPU01310300-02" : ['Blower', 'Conveyor'],
"01EPU01310300-20" : ['Blower', 'Conveyor'],
"01EPU01310300-18" : ['Blower', 'Conveyor'],
"01EPU01310300-16" : ['Blower', 'Conveyor'],
"01EPU01310300-06" : ['Blower', 'Conveyor'],
"01EPU01310300-12" : ['Blower', 'Conveyor'],
"01EPU01310300-17" : ['Blower', 'Conveyor'],
}

machine_part_static = {'3703' : {'M': ['1', '2'], 'F': ['3', '4']},
                '112RM044': {'M': ['1', '2'], 'F': ['3', '4']},
                '1115BC2': {'M': ['1', '2'], 'R': ['3', '4', '5', '6', '7', '8']},
                '2511ND1': {'M': ['1', '2'], 'R': ['3', '4', '5', '6', '7', '8']},
                '2511MD1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6', '7', '8']},
                '2511RM1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6', '7', '8']},
                '341-RM': {'M': ['1', '2'], 'F': ['3', '4']},
                '342-RM': {'M': ['1', '2'], 'F': ['3', '4']},
                'A-100': {'M': ['1', '2'], 'F': ['3', '4']},
                'R-102': {'M': ['1', '2'], 'F': ['3', '4']},
                'M-100': {'M': ['1', '2'], 'F': ['3', '4']},
                #=================================
                '04EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                '05EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                '06EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                '07EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                '08EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                '09EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                '10EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                '11EPU' : {'M': ['1', '2'], 'F': ['3', '4']},
                #====================
                '331.FN110' : {'M': ['1', '2'], 'F': ['3', '4']},
                '431.FN560' : {'M': ['1', '2'], 'F': ['3', '4']},
                #====================
                '2511-RM01': {'M': ['1', '2'], 'F': ['3', '4']},
                '113MF01': {'M': ['1', '2'], 'F': ['3', '4']},
                '341-MF': {'M': ['1', '2'], 'F': ['3', '4']},
                '2513FN1': {'M': ['1', '2'], 'F': ['3', '4']},
                'F-200': {'M': ['1', '2'], 'F': ['3', '4']},
                '121ID01': {'M': ['1', '2'], 'F': ['3', '4']},
                '450-FN': {'M': ['1', '2'], 'F': ['3', '4']},
                '3111FN1': {'M': ['1', '2'], 'F': ['3', '4']},
                '2403': {'M': ['1', '2'], 'F': ['3', '4']},
                'F-100': {'M': ['1', '2'], 'F': ['3', '4']},
                '122RK000': {'M': ['1', '2'], 'F': ['3', '4']},
                '431-KL': {'M': ['1', '2'], 'F': ['3', '4']},
                '3511MD1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6', '7', '8', '9', '10'], 'P' : ['11', '12']},
                'K-100': {'M': ['1', '2'], 'F': ['3', '4']},
                '125BELT': {'M': ['1', '2'], 'F': ['3', '4']},
                '146BELT': {'M': ['1', '2'], 'F': ['3', '4']},
                '275BELT': {'M': ['1', '2'], 'F': ['3', '4']},
                '283BELT': {'M': ['1', '2'], 'F': ['3', '4']},
                'AMUND-MAIN': {'M': ['1', '2'], 'F': ['3', '4']},
                'AMUND-RIJK': {'M': ['1', '2'], 'F': ['3', '4']},
                '010-BC': {'M': ['1', '2'], 'F': ['3', '4']},
                '020-BC': {'M': ['1', '2'], 'F': ['3', '4']},
                '130-BC': {'M': ['1', '2'], 'F': ['3', '4']},
                '221-BC': {'M': ['1', '2'], 'F': ['3', '4']},
                '511-BC': {'M': ['1', '2'], 'F': ['3', '4']},
                '1115BC2': {'M': ['1', '2'], 'F': ['3', '4']},
                '132BM01': {'M': ['1', '2'], 'F': ['3', '4']},
                'A-002': {'M': ['1', '2'], 'F': ['3', '4']},
                '133BM01': {'M': ['1', '2'], 'F': ['3', '4']},
                '232BM02': {'M': ['1', '2'], 'F': ['3', '4']},
                '233BM02': {'M': ['1', '2'], 'F': ['3', '4']},
                '531-BM': {'M': ['1', '2'], 'F': ['3', '4']},
                '532-BM': {'M': ['1', '2'], 'F': ['3', '4']},
                '5411BM1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6']},
                '5421BM1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6']},
                'A-300': {'M': ['1', '2'], 'F': ['3', '4']},
                'A-400': {'M': ['1', '2'], 'F': ['3', '4']},
                '5411MD1': {'M': ['1', '2'], 'F': ['3', '4']},
                'AMUND-CEME': {'M': ['1', '2'], 'F': ['3', '4']},
                '111-AP': {'M': ['1', '2'], 'F': ['3', '4']},
                '111-CR': {'M': ['1', '2'], 'F': ['3', '4']},
                '361-CR': {'M': ['1', '2'], 'F': ['3', '4']},
                '1112IM1': {'M': ['1', '2', '3', '4'], 'R': ['5', '6']},
                '1112IM3': {'M': ['1', '2', '3', '4'], 'R': ['5', '6']},
                '3612CR1': {'M': ['1', '2'], 'R': ['3', '4']},
                'C-100': {'M': ['1', '2'], 'F': ['3', '4']},
                'C-300': {'M': ['1', '2'], 'F': ['3', '4']},
                '210-RC': {'M': ['1', '2'], 'F': ['3', '4']},
                '341-SR': {'M': ['1', '2'], 'F': ['3', '4']},
                '531-SR': {'M': ['1', '2'], 'F': ['3', '4']},
                '532-SR': {'M': ['1', '2'], 'F': ['3', '4']},
                '2511SR1': {'M': ['1', '2'], 'F': ['3', '4']},
                '2513SR1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6', '7', '8', '9', '10'], 'R' : ['11']},
                '5413SR1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6', '7', '8'],'R' : ['9']},
                '5421SR1': {'M': ['1', '2'], 'F': ['3', '4']},
                '5423SR1': {'M': ['1', '2'], 'G': ['3', '4', '5', '6', '7', '8'],'R' : ['9']},
                '361-FN': {'M': ['1', '2'], 'F': ['3', '4']},
                '461-FN': {'M': ['1', '2'], 'F': ['3', '4']},
                '3218FN1': {'M': ['1', '2'], 'G' : ['3', '4' , '5', '6'], 'F': ['7', '8']},
                '3618FN1': {'M': ['1', '2'], 'F': ['3', '4']},
                'F-300': {'M': ['1', '2'], 'F': ['3', '4']},
                '412-EL': {'M': ['1', '2'], 'F': ['3', '4']},
                '5415BE1': {'M': ['1', '2'], 'F': ['3', '4']},
                '441-FN': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN0': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN1': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN2': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN3': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN4': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN5': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN6': {'M': ['1', '2'], 'F': ['3', '4']},
                '3611FN7': {'M': ['1', '2'], 'F': ['3', '4']},
                '501-RJ': {'M': ['1', '2'], 'F': ['3', '4']},
                '501-SI': {'M': ['1', '2'], 'F': ['3', '4']},
                '531-FN': {'M': ['1', '2'], 'F': ['3', '4']},
                '532-FN': {'M': ['1', '2'], 'F': ['3', '4']},
                '5413FN1': {'M': ['1', '2'], 'F': ['3', '4']},
                '5423FN1': {'M': ['1', '2'], 'F': ['3', '4']},
                'F-400': {'M': ['1', '2'], 'F': ['3', '4']},
                # ================================
                '501-RJ': {'M': ['1', '2'], 'G': ['3', '4', '5', '6', '7', '8', '9', '10']},
                #=================================
                'CP-BA48': {'M': ['1', '2'], 'F': ['3', '4']},
                #=======================
                '2516BL1': {'M': ['1', '2'], 'MILL' : ['3', '4', '5', '6']},
                '2516BL2': {'M': ['1', '2'], 'MILL' : ['3', '4', '5', '6']},
                '2516BL3': {'M': ['1', '2'], 'MILL' : ['3', '4', '5', '6']},
                '2816BL1': {'M': ['1', '2'], 'MILL' : ['3', '4', '5', '6']},
                '2816BL2': {'M': ['1', '2'], 'MILL' : ['3', '4', '5', '6']},
                '2816BL3': {'M': ['1', '2'], 'MILL' : ['3', '4', '5', '6']},
                '7411CP1': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7411CP2': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7411CP3': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7411CP4': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7411CP5': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7412CP1': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7412CP2': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7412CP3': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']},
                '7412CP4': {'M': ['1', '2'], 'G': ['3', '4'], 'C' : ['5', '6' , '7', '8']}}

machine_part_type = {
        "3111FN1": {
            "M": "Electromotor",
            "F": "Fan"
        },
        "3611FN1": {
            "M": "Electromotor",
            "F": "Fan"
        },
        "5423FN1": {
            "M": "Electromotor",
            "F": "Fan"
        },
        "2513FN1": {
            "M": "Electromotor",
            "F": "Fan"
        },
        "3618FN1": {
            "M": "Electromotor",
            "F": "Fan"
        },
        "5413FN1": {
            "M": "Electromotor",
            "F": "Fan"
        },
        "3218FN1": {
            "M": "Electromotor",
            "G": "Gearbox",
            "F": "Fan"
        }}
# =======================================================================================================================



class Wise:
  """
  This is a Library for SeeNous Corporation.\n
      self.machine_tag = # Machine Tag\n
      self.API_Get_Information()\n
      self.type = ['type']\n
      self.kind = ['kind']\n
      self.power = ['power']\n
      self.foundation = ['foundation']\n
      self.rpm = ['rpm']\n
      self.machine_part = ['Machine_part']\n
      self.weight = ['Customer_failure_weight']\n
  Have Fun with Capability ;)
  """
  # Initialize
  def __init__(self, machine_tag:str, static=False):
      """
      Initialize the Wise class.
      
      :param machine_tag: The tag of the machine to analyze.
      :param static: Whether to use static information (default is True).
      """
      failures = ['Unbalance', 'Looseness', 'Misalignment', 'Coupling', 'Bearing', 'Gearbox'] # List of failure we can detected so far
      self.machine_tag = machine_tag
      # Check for get static information or from API
      if static:
          self.static_Get_Information()
      else:
          self.dynamic_Get_Information()
      # Find failures for machine
      self.failures = failures # List of failure we can detected so far
      self.points = self.all_points() # Make a list of all points
      self.equipments_included_failure()
      self.rpm_separator()

  # Wellcome Pack
  def Wellcome(self):
      # Set up the turtle speed and background
      speed(0)  # Fastest speed
      bgcolor("black")

      # Write the text above the animation
      penup()
      goto(0, 200)  # Move to the top center
      color("white")
      style = ("Arial", 20, "bold")
      write("Welcome to Wisdom my friend.", align="center", font=style)
      goto(0, 0)  # Return to the center
      pendown()

      # Initialize color hue
      h = 0
      for i in range(16):
          for j in range(18):
              c = colorsys.hsv_to_rgb(h, 1, 1)  # Generate RGB color
              color(c)
              h += 0.005  # Increment hue
              rt(90)
              circle(150 - j * 6, 90)
              lt(90)
              circle(150 - j * 6, 90)
              rt(180)
          circle(40, 24)
      done()

  # Find all points
  def all_points(self):
      """
      Find all points of the machine.
      """
      lst_all_points = list()
      for spare in self.machine_part:
          lst_points = self.machine_part[spare]
          for point in lst_points:
              lst_all_points.append(point)
      return lst_all_points

  # Seperate RPM per point in High / Mid / Low
  def rpm_separator(self):
      """
      Seperate RPM per point in High / Mid / Low
      """
      # Make variable
      self.High_rpm_points = list()
      self.Mid_rpm_points = list()
      self.Low_rpm_points = list()
      # Iterate in points
      for point in self.points:
          rpm = float(self.rpm[point]['value'])
          if rpm <= 120:
              self.Low_rpm_points.append(point)
          elif rpm <= 300:
              self.Mid_rpm_points.append(point)
          else:
              self.High_rpm_points.append(point)

  # Find list of failure detection for failures
  def equipments_included_failure(self):
      """
      Find list of failure detection for failures
      """
      if ('Fan' not in self.machine_type) and ('Pump' not in self.machine_type):
          if 'Unbalance' not in self.failures:
              pass
          else:
              self.failures.remove('Unbalance')

  # Get machine part in pandex format
  def get_machine_part_pandex(self):
    """
    Get machine part in pandex format.
    """
    machine_part_pandex = dict()
    for spare in self.machine_part:
        for point in self.machine_part[spare]:
            machine_part_pandex[point] = spare
    return machine_part_pandex
  
  def static_Get_Information(self):
      """
      Get static information of the machine.
      """
      self.machine_tag = self.machine_tag # Machine Tag
      self.type_kind = equipments_typ[self.machine_tag] # What is the machine
      self.machine_type = equipments_typ[self.machine_tag][1] # what`s machine type
      self.kind = fan_type[self.machine_tag] # What`s the machine kind
      self.power = power[self.machine_tag] # Power of machine (kw) 
      self.foundation = foundation[self.machine_tag] # Foundation of machine
      self.rpm = rpm[self.machine_tag] # RPM
      self.weight = Detail['Customer_failure_weight'] # Failure weights based on rpm group
      self.machine_part = machine_part_static[self.machine_tag] # Machine part
      self.machine_part_type = machine_part_type[self.machine_tag] # Machine part type
      self.information = 'Static'
  
  # Get Information from Database
  def dynamic_Get_Information(self):
      """
      Get information from the database.
      """
      # Load json
      with open("/Users/fateme/Desktop/CeeNous/Backtest Automation/data/machin_info.json", 'r') as file:
        data = json.load(file)  # "load" = load from file      
      
      machine_tag = self.machine_tag # Machine Tag
      self.machine_type = data['machine_type'][machine_tag] # what`s machine type
      self.type_kind = equipments_typ[self.machine_tag] # What is the machine
      self.machine_name = data['machine_name'][machine_tag] # what`s machine name
      self.priority = data['priority'][machine_tag] # what`s machine priority
      self.data_collection_period = data['data_collection_period'][machine_tag]
      self.kind = data['fan_type'][machine_tag] # What`s the machine kind 
      self.power = data['power'][machine_tag] # Power of machine (kw)
      self.foundation = data['foundation'][machine_tag] # Foundation of machine
      self.rpm = data['rpm'][machine_tag] # RPM
      self.point_id = data['point_id'][machine_tag] # Adding point id
    #   self.weight = data['Customer_failure_weight'][self.machine_tag] # Failures weight     
      self.weight = data['Customer_failure_weight'][machine_tag] # Failure weights based on rpm group
      self.machine_part = data['machine_part_static'][machine_tag] # Machine part
      self.machine_part_type = data['machine_part_type'][machine_tag] # Machine part type
      self.bearings = data['bearing'][machine_tag] # Machine part type
      self.information = 'Dynamic'



# Test
# info = Wise('01EPU01310300-15')
# print(info.failures)


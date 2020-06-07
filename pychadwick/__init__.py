from pandas import Int32Dtype
from pychadwick.libutils import ChadwickLibrary

_version = "0.2.0"

__all__ = ["ChadwickLibrary"]

nullable_int = Int32Dtype()

EVENT_DATA_TYPES = {
    "GAME_ID": str,
    "AWAY_TEAM_ID": str,
    "INN_CT": nullable_int,
    "BAT_HOME_ID": nullable_int,
    "OUTS_CT": nullable_int,
    "BALLS_CT": nullable_int,
    "STRIKES_CT": nullable_int,
    "PITCH_SEQ_TX": str,
    "AWAY_SCORE_CT": nullable_int,
    "HOME_SCORE_CT": nullable_int,
    "BAT_ID": str,
    "BAT_HAND_CD": str,
    "RESP_BAT_ID": str,
    "RESP_BAT_HAND_CD": str,
    "PIT_ID": str,
    "PIT_HAND_CD": str,
    "RESP_PIT_ID": str,
    "RESP_PIT_HAND_CD": str,
    "POS2_FLD_ID": str,
    "POS3_FLD_ID": str,
    "POS4_FLD_ID": str,
    "POS5_FLD_ID": str,
    "POS6_FLD_ID": str,
    "POS7_FLD_ID": str,
    "POS8_FLD_ID": str,
    "POS9_FLD_ID": str,
    "BASE1_RUN_ID": str,
    "BASE2_RUN_ID": str,
    "BASE3_RUN_ID": str,
    "EVENT_TX": str,
    "LEADOFF_FL": str,
    "PH_FL": str,
    "BAT_FLD_CD": nullable_int,
    "BAT_LINEUP_ID": nullable_int,
    "EVENT_CD": nullable_int,
    "BAT_EVENT_FL": str,
    "AB_FL": str,
    "H_CD": nullable_int,
    "SH_FL": str,
    "SF_FL": str,
    "EVENT_OUTS_CT": nullable_int,
    "DP_FL": str,
    "TP_FL": str,
    "RBI_CT": nullable_int,
    "WP_FL": str,
    "PB_FL": str,
    "FLD_CD": nullable_int,
    "BATTEDBALL_CD": str,
    "BUNT_FL": str,
    "FOUL_FL": str,
    "BATTEDBALL_LOC_TX": str,
    "ERR_CT": nullable_int,
    "ERR1_FLD_CD": nullable_int,
    "ERR1_CD": str,
    "ERR2_FLD_CD": nullable_int,
    "ERR2_CD": str,
    "ERR3_FLD_CD": nullable_int,
    "ERR3_CD": str,
    "BAT_DEST_ID": nullable_int,
    "RUN1_DEST_ID": nullable_int,
    "RUN2_DEST_ID": nullable_int,
    "RUN3_DEST_ID": nullable_int,
    "BAT_PLAY_TX": str,
    "RUN1_PLAY_TX": str,
    "RUN2_PLAY_TX": str,
    "RUN3_PLAY_TX": str,
    "RUN1_SB_FL": str,
    "RUN2_SB_FL": str,
    "RUN3_SB_FL": str,
    "RUN1_CS_FL": str,
    "RUN2_CS_FL": str,
    "RUN3_CS_FL": str,
    "RUN1_PK_FL": str,
    "RUN2_PK_FL": str,
    "RUN3_PK_FL": str,
    "RUN1_RESP_PIT_ID": str,
    "RUN2_RESP_PIT_ID": str,
    "RUN3_RESP_PIT_ID": str,
    "GAME_NEW_FL": str,
    "GAME_END_FL": str,
    "PR_RUN1_FL": str,
    "PR_RUN2_FL": str,
    "PR_RUN3_FL": str,
    "REMOVED_FOR_PR_RUN1_ID": str,
    "REMOVED_FOR_PR_RUN2_ID": str,
    "REMOVED_FOR_PR_RUN3_ID": str,
    "REMOVED_FOR_PH_BAT_ID": str,
    "REMOVED_FOR_PH_BAT_FLD_CD": nullable_int,
    "PO1_FLD_CD": nullable_int,
    "PO2_FLD_CD": nullable_int,
    "PO3_FLD_CD": nullable_int,
    "ASS1_FLD_CD": nullable_int,
    "ASS2_FLD_CD": nullable_int,
    "ASS3_FLD_CD": nullable_int,
    "ASS4_FLD_CD": nullable_int,
    "ASS5_FLD_CD": nullable_int,
    "HOME_TEAM_ID": str,
    "BAT_TEAM_ID": str,
    "FLD_TEAM_ID": str,
    "BAT_LAST_ID": nullable_int,
    "INN_NEW_FL": str,
    "INN_END_FL": str,
    "START_BAT_SCORE_CT": nullable_int,
    "START_FLD_SCORE_CT": nullable_int,
    "INN_RUNS_CT": nullable_int,
    "GAME_PA_CT": nullable_int,
    "INN_PA_CT": nullable_int,
    "PA_NEW_FL": str,
    "PA_TRUNC_FL": str,
    "START_BASES_CD": nullable_int,
    "END_BASES_CD": nullable_int,
    "BAT_START_FL": str,
    "RESP_BAT_START_FL": str,
    "BAT_ON_DECK_ID": str,
    "BAT_IN_HOLD_ID": str,
    "PIT_START_FL": str,
    "RESP_PIT_START_FL": str,
    "RUN1_FLD_CD": nullable_int,
    "RUN1_LINEUP_CD": nullable_int,
    "RUN1_ORIGIN_EVENT_ID": nullable_int,
    "RUN2_FLD_CD": nullable_int,
    "RUN2_LINEUP_CD": nullable_int,
    "RUN2_ORIGIN_EVENT_ID": nullable_int,
    "RUN3_FLD_CD": nullable_int,
    "RUN3_LINEUP_CD": nullable_int,
    "RUN3_ORIGIN_EVENT_ID": nullable_int,
    "RUN1_RESP_CAT_ID": str,
    "RUN2_RESP_CAT_ID": str,
    "RUN3_RESP_CAT_ID": str,
    "PA_BALL_CT": nullable_int,
    "PA_CALLED_BALL_CT": nullable_int,
    "PA_INTENT_BALL_CT": nullable_int,
    "PA_PITCHOUT_BALL_CT": nullable_int,
    "PA_HITBATTER_BALL_CT": nullable_int,
    "PA_OTHER_BALL_CT": nullable_int,
    "PA_STRIKE_CT": nullable_int,
    "PA_CALLED_STRIKE_CT": nullable_int,
    "PA_SWINGMISS_STRIKE_CT": nullable_int,
    "PA_FOUL_STRIKE_CT": nullable_int,
    "PA_INPLAY_STRIKE_CT": nullable_int,
    "PA_OTHER_STRIKE_CT": nullable_int,
    "EVENT_RUNS_CT": nullable_int,
    "FLD_ID": str,
    "BASE2_FORCE_FL": str,
    "BASE3_FORCE_FL": str,
    "BASE4_FORCE_FL": str,
    "BAT_SAFE_ERR_FL": str,
    "BAT_FATE_ID": nullable_int,
    "RUN1_FATE_ID": nullable_int,
    "RUN2_FATE_ID": nullable_int,
    "RUN3_FATE_ID": nullable_int,
    "FATE_RUNS_CT": nullable_int,
    "ASS6_FLD_CD": nullable_int,
    "ASS7_FLD_CD": nullable_int,
    "ASS8_FLD_CD": nullable_int,
    "ASS9_FLD_CD": nullable_int,
    "ASS10_FLD_CD": nullable_int,
    "UNKNOWN_OUT_EXC_FL": str,
    "UNCERTAIN_PLAY_EXC_FL": str,
}

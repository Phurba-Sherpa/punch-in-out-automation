from datetime import datetime, time

PUNCH_IN_TIME_MAX_TH= time(11, 0, 0)            # Max threashold time for punch in (11:00:00)
PUNC_OUT_TIME_MIN_TH = time(6, 0, 0)            # Min. threshold time for punch out (6:00:00)
OPERATION_TYPES = {
    'PUNCH_IN': 'PI',
    'PUNCH_OUT': 'PO'
}

def get_operation_type():
    """
    Return the action type: punch in/out.
    If it is before 11:00:00 then PI (PUNCH IN)
    If it is after 06:00:00 then PO (PUNCH OUT)
    """

    current_time = datetime.now().time()
    if current_time <= PUNCH_IN_TIME_MAX_TH:
        return OPERATION_TYPES.get('PUNCH_IN')
    elif current_time > PUNC_OUT_TIME_MIN_TH:
        return OPERATION_TYPES.get('PUNCH_OUT')
    
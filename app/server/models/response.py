def response_model(data, message):
    '''
    API Response: successful <200>
    '''
    if(isinstance(data, list)):
        return {
            "data": data,
            "code": 200,
            "message": message,
        }
    else:
        return {
            "data": [data],
            "code": 200,
            "message": message,
        }


def error_response_model(error, code, message):
    '''
    API Error Response
    '''
    return {
        "error": error,
        "code": code,
        "message": message
        }

def divide(divident, divisor):
    try:
        result = divident // divisor
        return int(result)
    
    except ZeroDivisionError:
        raise
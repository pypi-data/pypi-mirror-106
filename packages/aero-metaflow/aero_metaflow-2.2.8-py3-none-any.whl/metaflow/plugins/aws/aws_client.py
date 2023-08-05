
def get_aws_client(module, with_error=False, params={}):
    from metaflow.exception import MetaflowException
    import requests

    try:
        import boto3
        from botocore.exceptions import ClientError
    except (NameError, ImportError):
        raise MetaflowException(
            "Could not import module 'boto3'. Install boto3 first.")

    if with_error:
        return boto3.client(module, **params), ClientError
    return boto3.client(module, **params)

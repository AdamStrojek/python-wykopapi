import hashlib

__author__ = 'astrojek'


def build_api_params(api_params):
    result = []

    for key, value in api_params.iteritems():
        result.append('{key},{value}'.format(
            key=key,
            value=value
        ))

    return ','.join(result)


def build_post_params():
    pass


def sign_post_params(secret, url, post_params):
    m = hashlib.new('md5')
    m.update(secret)
    m.update(url)

    for key in sorted(post_params.keys()):
        m.update(post_params[key])

    return m.hexdigest()


def build_url():
    pass

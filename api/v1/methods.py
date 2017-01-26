from flask import jsonify

from api import cache
from api.v1 import v1


def calculate_fib(n):
    result = [0, 1]
    for i in range(2, n + 1):
        result.append(result[-1] + result[-2])
    return result


@v1.route('/fib/<number>', methods=['GET', ])
def fib(number):

    try:
        number = int(number)
    except ValueError:
        return jsonify({'error': 'Not an integer.'})

    if number > 1000:
        return jsonify({'error': 'Try a number less than 1000.'})
    result = cache.get(number)

    if result is None:
        result = calculate_fib(number)
        cache.set(number, result, timeout=60 * 60)

    return jsonify({'sequence': result})


@v1.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Invalid API call.'}), 404

import configuration
import requests
import data


# создание нового заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)


# получение трек id
def get_track_id():
    return post_new_order(data.order_body).json().get('track')


def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFORMATION_PATH + str(get_track_id()))





from OdooLocust import OdooLocustUser
from OdooLocust import OdooTaskSet


class Seller(OdooLocustUser.OdooLocustUser):
    database = "locusttestdb"
    login = "admin"
    password = "admin"

    tasks = [OdooTaskSet.OdooGenericTaskSet]

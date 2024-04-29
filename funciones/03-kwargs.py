""" Keywords arguments """

def get_products(**kwargs):
    print(kwargs["id"])
    print(kwargs["name"])
    
    
get_products(id=23,
             name="Iphone"
             )
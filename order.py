# order_processor.py

def process_order(order, tax_rate, discount_code):
    # order is expected to be a dict like:
    # {"items": [{"name": "Pen", "price": 10, "qty": 2}, ...], "customer_type": "regular"}

    total = 0
    for i in order["items"]:
        total = total + (i["price"] * i["qty"])

    # discount
    discount = 0
    if discount_code != None:
        if discount_code == "SAVE10":
            discount = total * 0.10
        elif discount_code == "SAVE20":
            if order["customer_type"] == "vip":
                discount = total * 0.20
            else:
                discount = total * 0.05
        else:
            discount = 0

    # tax
    tax = (total - discount) * tax_rate

    # shipping
    shipping = 0
    if total - discount > 100:
        shipping = 0
    else:
        shipping = 10

    grand_total = (total - discount) + tax + shipping

    result = {}
    result["subtotal"] = total
    result["discount"] = discount
    result["tax"] = tax
    result["shipping"] = shipping
    result["grand_total"] = grand_total
    return result


if __name__ == "__main__":
    sample_order = {
        "items": [{"name": "Pen", "price": 10, "qty": 2}, {"name": "Notebook", "price": 50, "qty": 1}],
        "customer_type": "vip"
    }
    print(process_order(sample_order, 0.18, "SAVE20"))
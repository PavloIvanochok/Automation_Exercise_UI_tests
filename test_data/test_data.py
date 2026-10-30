import random


class TestData:
    __test__ = False

    def __init__(self):
        self.product = random.choice([
            {"id": "1", "name": "Blue Top", "price": "Rs. 500"},
            {"id": "2", "name": "Men Tshirt", "price": "Rs. 400"},
            {"id": "3", "name": "Sleeveless Dress", "price": "Rs. 1000"},
            {"id": "4", "name": "Stylish Dress", "price": "Rs. 1500"},
            {"id": "5", "name": "Winter Top", "price": "Rs. 600"},
            {"id": "6", "name": "Summer White Top", "price": "Rs. 400"},
            {"id": "7", "name": "Madame Top For Women", "price": "Rs. 1000"},
            {"id": "8", "name": "Fancy Green Top", "price": "Rs. 700"},
            {"id": "11", "name": "Sleeves Printed Top - White", "price": "Rs. 499"},
            {"id": "12", "name": "Half Sleeves Top Schiffli Detailing - Pink", "price": "Rs. 359"},
            {"id": "13", "name": "Frozen Tops For Kids", "price": "Rs. 278"},
            {"id": "14", "name": "Full Sleeves Top Cherry - Pink", "price": "Rs. 679"},
            {"id": "15", "name": "Printed Off Shoulder Top - White", "price": "Rs. 315"},
            {"id": "16", "name": "Sleeves Top and Short - Blue & Pink", "price": "Rs. 478"},
            {"id": "18", "name": "Little Girls Mr. Panda Shirt", "price": "Rs. 1200"},
            {"id": "19", "name": "Sleeveless Unicorn Patch Gown - Pink", "price": "Rs. 1050"},
            {"id": "20", "name": "Cotton Mull Embroidered Dress", "price": "Rs. 1190"},
            {"id": "21", "name": "Blue Cotton Indie Mickey Dress", "price": "Rs. 1530"},
            {"id": "22", "name": "Long Maxi Tulle Fancy Dress Up Outfits -Pink", "price": "Rs. 1600"},
            {"id": "23", "name": "Sleeveless Unicorn Print Fit & Flare Net Dress - Multi", "price": "Rs. 1100"},
            {"id": "24", "name": "Colour Blocked Shirt - Sky Blue", "price": "Rs. 849"},
            {"id": "28", "name": "Pure Cotton V-Neck T-Shirt", "price": "Rs. 1299"},
            {"id": "29", "name": "Green Side Placket Detail T-Shirt", "price": "Rs. 1000"},
            {"id": "30", "name": "Premium Polo T-Shirts", "price": "Rs. 1500"},
            {"id": "31", "name": "Pure Cotton Neon Green Tshirt", "price": "Rs. 850"},
            {"id": "33", "name": "Soft Stretch Jeans", "price": "Rs. 799"},
            {"id": "35", "name": "Regular Fit Straight Jeans", "price": "Rs. 1200"},
            {"id": "37", "name": "Grunt Blue Slim Fit Jeans", "price": "Rs. 1400"},
            {"id": "38", "name": "Rose Pink Embroidered Maxi Dress", "price": "Rs. 2300"},
            {"id": "39", "name": "Cotton Silk Hand Block Print Saree", "price": "Rs. 3000"},
            {"id": "40", "name": "Rust Red Linen Saree", "price": "Rs. 3500"},
            {"id": "41", "name": "Beautiful Peacock Blue Cotton Linen Saree", "price": "Rs. 5000"},
            {"id": "42", "name": "Lace Top For Women", "price": "Rs. 1400"},
            {"id": "43", "name": "GRAPHIC DESIGN MEN T SHIRT - BLUE", "price": "Rs. 1389"}
        ])

        self.quantity = random.randint(1, 20)

        self.card_data = {
            "name_on_card": "Test User",
            "card_number": "4111111111111111",
            "cvc": "123",
            "expiry_month": "12",
            "expiry_year": "2030"
        }

        self.recommended_product = random.choice([
            {"id": "1", "name": "Blue Top", "price": "Rs. 500"},
            {"id": "2", "name": "Men Tshirt", "price": "Rs. 400"},
            {"id": "4", "name": "Stylish Dress", "price": "Rs. 1500"},
            {"id": "5", "name": "Winter Top", "price": "Rs. 600"},
            {"id": "6", "name": "Summer White Top", "price": "Rs. 400"}
        ])

        self.non_existent_product = random.choice([
            "InvalidProductXYZ123",
            "NonExistentItem456",
            "UnknownProduct789",
            "TestProductNotFound",
            "ProductDoesNotExist999",
            "RandomItemABC987",
            "MissingProduct000",
            "NoSuchProductXYZ",
            "FakeProduct12345",
            "UndefinedItem567"
        ])

        self.brand = random.choice([
            "H&M",
            "Madame",
            "Mast & Harbour",
            "Babyhug",
            "Allen Solly Junior",
            "Kookie Kids",
            "Biba"
        ])

        self.selected_item = random.choice([
            {"name": "Women", "subcategories": ["Dress", "Tops", "Saree"]},
            {"name": "Men", "subcategories": ["Tshirts", "Jeans"]},
            {"name": "Kids", "subcategories": ["Dress", "Tops & Shirts"]}])

        self.category = self.selected_item["name"]
        
        self.subcategory = random.choice(self.selected_item["subcategories"])
    
        

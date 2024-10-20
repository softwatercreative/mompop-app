from django.db import models


class Shops(models.Model):
    COUNTIES_LIST = [
        ("001", "Allegany County"),
        ("002", "Anne Arundel County"),
        ("003", "Baltimore County"),
        ("004", "Calvert County"),
        ("005", "Caroline County"),
        ("006", "Carroll County"),
        ("007", "Cecil County"),
        ("008", "Charles County"),
        ("009", "Dorchester County"),
        ("010", "Frederick County"),
        ("011", "Garrett County"),
        ("012", "Harford County"),
        ("013", "Howard County"),
        ("014", "Kent County"),
        ("015", "Montgomery County"),
        ("016", "Prince George's County"),
        ("017", "Queen Anne's County"),
        ("018", "St. Mary's County"),
        ("019", "Somerset County"),
        ("020", "Talbot County"),
        ("021", "Washington County"),
        ("022", "Wicomico County"),
        ("023", "Worcester County"),
        ("030", "Baltimore City"),
    ]
    
    
    SHOPS_LIST = [
        ("ART", "Artist/Crafts/Gift Shop"),
        ("BRB", "Barber"),
        ("BAK", "Baking Company"),
        ("CC", "Child Care"),
        ("EDU", "Educational Services/Tutoring"),
        ("SSL", "Spa/Salon"),
        ("CFT", "Crafts"),
        ("LAN", "Landscaping"),
        ("MOV", "Moving/Delivery"),
        ("PET", "Pet Care/Products"),
        ("PIC", "Photography"),
        ("REL", "Real Estate/Rental/Leasing"),
        ("RTL", "Retail/Trade"),
        ("SPT", "Sports/Training/Fitness"),
        ("OTH", "Other"),
    ]
    
    name = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    county = models.CharField(max_length=3, choices=COUNTIES_LIST)
    type = models.CharField(max_length=3, choices=SHOPS_LIST)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Add business image capabilites
     
    def __str__(self):
        return f"{self.business_name} ({self.get_type_display()})"

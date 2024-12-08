from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    image_url = models.CharField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_resolved = models.BooleanField(default=False)
    resolved_comment = models.ForeignKey(
        'Comment', on_delete=models.SET_NULL, null=True, blank=True, related_name='resolved_for_post'
    )

    # New fields with predefined choices
    COLOR_CHOICES = [
        ('red', 'Red'),  
        ('blue', 'Blue'),  
        ('yellow', 'Yellow'),  
        ('green', 'Green'),  
        ('orange', 'Orange'),  
        ('purple', 'Purple'),  
        ('red-orange', 'Red-Orange'),  
        ('yellow-orange', 'Yellow-Orange'),  
        ('yellow-green', 'Yellow-Green'),  
        ('blue-green', 'Blue-Green'),  
        ('blue-purple', 'Blue-Purple'),  
        ('red-purple', 'Red-Purple'),  
        ('black', 'Black'),  
        ('white', 'White'),
        ('beige', 'Beige'),
        ('gray', 'Gray'),  
        ('brown', 'Brown'),  
        ('pink', 'Pink'),  
        ('cyan', 'Cyan'),  
        ('magenta', 'Magenta'),  
        ('beige', 'Beige'),  
        ('teal', 'Teal'),  
        ('lavender', 'Lavender'),  
        ('maroon', 'Maroon'),  
        ('navy', 'Navy'),  
        ('olive', 'Olive'),  
        ('gold', 'Gold'),  
        ('silver', 'Silver'),
        ('other', 'Other'),
    ]

    SHAPE_CHOICES = [
        ('circle', 'Circle'),  
        ('square', 'Square'),  
        ('rectangle', 'Rectangle'),  
        ('triangle', 'Triangle'),  
        ('oval', 'Oval'),  
        ('pentagon', 'Pentagon'),  
        ('hexagon', 'Hexagon'),  
        ('heptagon', 'Heptagon'),  
        ('octagon', 'Octagon'),  
        ('nonagon', 'Nonagon'),  
        ('decagon', 'Decagon'),  
        ('cube', 'Cube'),  
        ('cuboid', 'Cuboid'),  
        ('sphere', 'Sphere'),  
        ('cylinder', 'Cylinder'),  
        ('cone', 'Cone'),  
        ('pyramid', 'Pyramid'),  
        ('prism', 'Prism'),  
        ('torus', 'Torus'),  
        ('star', 'Star'),  
        ('heart', 'Heart'),  
        ('diamond', 'Diamond'),  
        ('parallelogram', 'Parallelogram'),  
        ('trapezoid', 'Trapezoid'),  
        ('rhombus', 'Rhombus'),  
        ('crescent', 'Crescent'),  
        ('arrow', 'Arrow'),
        ('other', 'Other'),
    ]

    MATERIAL_CHOICES = [
        ('wood', 'Wood'),  
        ('metal', 'Metal'),  
        ('plastic', 'Plastic'),  
        ('glass', 'Glass'),  
        ('stone', 'Stone'),  
        ('ceramic', 'Ceramic'),  
        ('fabric', 'Fabric'),  
        ('leather', 'Leather'),  
        ('rubber', 'Rubber'),  
        ('paper', 'Paper'),  
        ('cardboard', 'Cardboard'),  
        ('concrete', 'Concrete'),  
        ('brick', 'Brick'),  
        ('foam', 'Foam'),  
        ('carbon-fiber', 'Carbon-Fiber'),  
        ('kevlar', 'Kevlar'),  
        ('silicone', 'Silicone'),  
        ('clay', 'Clay'),  
        ('wax', 'Wax'),  
        ('gold', 'Gold'),  
        ('silver', 'Silver'),  
        ('copper', 'Copper'),  
        ('aluminum', 'Aluminum'),  
        ('iron', 'Iron'),  
        ('steel', 'Steel'),  
        ('bronze', 'Bronze'),  
        ('brass', 'Brass'),
        ('other', 'Other'),
    ]

    WEIGHT_CHOICES = [
        ('0-2.5kg', '0-2.5kg'),
        ('2.5-5kg', '2.5-5kg'),
        ('5-10kg', '5-10kg'),
        ('other', 'Other'),
    ]

    LOCATION_CHOICES = [
        ('europe', 'Europe'),
        ('asia', 'Asia'),
        ('north america', 'North America'),
        ('south america', 'South America'),
        ('africa', 'Africa'),
        ('australia', 'Australia'),
        ('antarctica', 'Antarctica'),
        ('other', 'Other'),
    ]

    HARDNESS_CHOICES = [
        ('soft', 'Soft'),  
        ('medium-soft', 'Medium-Soft'),  
        ('medium', 'Medium'),  
        ('medium-hard', 'Medium-Hard'),  
        ('hard', 'Hard'),  
        ('very-hard', 'Very-Hard'),
        ('rigid', 'Rigid'),
        ('other', 'Other'),
    ]

    TIME_PERIOD_CHOICES = [
        ('medieval era', 'Medieval Era'),
        ('early modern era', 'Early Modern Era'),
        ('prehistoric', 'Prehistoric'),  
        ('stone age', 'Stone Age'),  
        ('bronze-age', 'Bronze Age'),  
        ('iron age', 'Iron Age'),  
        ('classical era', 'Classical Era'),  
        ('middle-ages', 'Middle Ages'),  
        ('renaissance', 'Renaissance'),  
        ('age-of-exploration', 'Age of Exploration'),  
        ('industrial-age', 'Industrial Age'),  
        ('modern era', 'Modern Era'),  
        ('information-age', 'Information Age'),  
        ('paleozoic-era', 'Paleozoic Era'),  
        ('mesozoic-era', 'Mesozoic Era'),  
        ('cenozoic-era', 'Cenozoic Era'),  
        ('jurassic-period', 'Jurassic Period'),  
        ('cretaceous-period', 'Cretaceous Period'),  
        ('pleistocene-epoch', 'Pleistocene Epoch'),  
        ('holocene-epoch', 'Holocene Epoch'),
        ('other', 'Other'),
    ]
    
    SMELL_CHOICES = [
        ('woody', 'Woody'),
        ('fragrant', 'Fragrant'),
        ('fruity', 'Fruity'),
        ('minty', 'Minty'),
        ('sweet', 'Sweet'),
        ('popcorn', 'Popcorn'),
        ('lemon', 'Lemon'),
        ('chemical', 'Chemical'),
        ('pungent', 'Pungent'),
        ('decayed', 'Decayed'),
        ('none', 'None'),
        ('other', 'Other'),
    ]

    TASTE_CHOICES = [
        ('sweet', 'Sweet'),
        ('sour', 'Sour'),
        ('bitter', 'Bitter'),
        ('salty', 'Salty'),
        ('umami', 'Umami'),
        ('savory', 'Savory'),
        ('other', 'Other'),
    ]

    TEXTURE_CHOICES = [
        ('smooth', 'Smooth'),
        ('rough', 'Rough'),
        ('grainy', 'Grainy'),
        ('slimy', 'Slimy'),
        ('slippery', 'Slippery'),  
        ('matte', 'Matte'),  
        ('glossy', 'Glossy'),  
        ('bumpy', 'Bumpy'),  
        ('gritty', 'Gritty'),  
        ('velvety', 'Velvety'),  
        ('fuzzy', 'Fuzzy'),  
        ('silky', 'Silky'),  
        ('coarse', 'Coarse'),  
        ('pebbled', 'Pebbled'),  
        ('polished', 'Polished'),  
        ('woven', 'Woven'),  
        ('hairy', 'Hairy'),  
        ('sticky', 'Sticky'),  
        ('spongy', 'Spongy'),  
        ('crispy', 'Crispy'),  
        ('wrinkled', 'Wrinkled'),  
        ('slick', 'Slick'),  
        ('pitted', 'Pitted'),  
        ('corrugated', 'Corrugated'),
        ('other', 'Other'),
    ]

    VALUE_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('luxury', 'Luxury'),
        ('fragile', 'Fragile'),  
        ('durable', 'Durable'),  
        ('lightweight', 'Lightweight'),  
        ('heavy', 'Heavy'),  
        ('expensive', 'Expensive'),  
        ('affordable', 'Affordable'),  
        ('luxurious', 'Luxurious'),  
        ('eco-friendly', 'Eco-Friendly'),  
        ('recyclable', 'Recyclable'),  
        ('disposable', 'Disposable'),  
        ('handcrafted', 'Handcrafted'),  
        ('mass-produced', 'Mass-Produced'),  
        ('versatile', 'Versatile'),  
        ('customizable', 'Customizable'),  
        ('limited-edition', 'Limited Edition'),  
        ('unique', 'Unique'),  
        ('high-quality', 'High-Quality'),  
        ('low-quality', 'Low-Quality'),  
        ('rare', 'Rare'),  
        ('common', 'Common'),  
        ('portable', 'Portable'),  
        ('compact', 'Compact'),  
        ('ergonomic', 'Ergonomic'),  
        ('innovative', 'Innovative'),  
        ('traditional', 'Traditional'),
        ('other', 'Other'),
    ]

    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='other')
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES, default='other')
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default='other')
    weight = models.CharField(max_length=20, choices=WEIGHT_CHOICES, default='other')
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES, default='other')
    hardness = models.CharField(max_length=20, choices=HARDNESS_CHOICES, default='other')
    time_period = models.CharField(max_length=20, choices=TIME_PERIOD_CHOICES, default='other')
    smell = models.CharField(max_length=20, choices=SMELL_CHOICES, default='other')
    taste = models.CharField(max_length=20, choices=TASTE_CHOICES, default='other')
    texture = models.CharField(max_length=20, choices=TEXTURE_CHOICES, default='other')
    value = models.CharField(max_length=20, choices=VALUE_CHOICES, default='other')
    # New size fields
    height = models.PositiveIntegerField(null=True, blank=True)
    length = models.PositiveIntegerField(null=True, blank=True)
    depth = models.PositiveIntegerField(null=True, blank=True)
    SIZE_UNITS = [
        ('cm', 'Centimeters'),
        ('inch', 'Inches'),
    ]
    size_unit = models.CharField(max_length=10, choices=SIZE_UNITS, default='cm')


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
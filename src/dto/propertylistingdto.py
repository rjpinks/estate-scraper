class PropertyListingDto():
    id: int
    address: str
    bedrooms: int
    bathrooms: int
    square_feet: int
    acres: float
    listing_id: int
    year_built: int
    floors: int
    garage: bool
    rural: bool
    price: float
    hoa: bool
    photos: str
    url: str

    def __init__(
            self, id, address, bedrooms, bathrooms,
            square_feet, acres, listing_id, year_built,
            floors, garage, rural, price, hoa, photos, url
            ) -> None:
        self.id = id
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.square_feet = square_feet
        self.acres = acres
        self.listing_id = listing_id
        self.year_built = year_built
        self.floors = floors
        self.garage = garage
        self.rural = rural
        self.price = price
        self.hoa = hoa
        self.url = url
        self.photos = photos

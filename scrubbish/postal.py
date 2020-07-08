class Postal:
    def __init__(self, address):
        self.address = address.strip(" ")

    def info(self):
        district = self._district()

        if district in self._codes():
            district_info = self._codes()[district]
            result = {"district": district}
            result.update(district_info)

            return result

        return self._empty()

    def _district(self):
        district = self._code().split(" ")[0].lower()
        if district.startswith("bt"):
            return district

        return "?"

    def _code(self):
        return " ".join(self.address.split(" ")[-2:])

    def _empty(self):
        return {
            "district": self._district(),
            "position": "?",
            "post_town": "?",
            "coverage": "?",
        }

    def _codes(self):
        return {
            "bt1": {
                "position": "centre",
                "post_town": "Belfast",
                "coverage": "Belfast",
            },
            "bt2": {
                "position": "centre",
                "post_town": "Belfast",
                "coverage": "Belfast",
            },
            "bt3": {
                "position": "north",
                "post_town": "Belfast",
                "coverage": "Belfast, Docks",
            },
            "bt4": {
                "position": "east",
                "post_town": "Belfast",
                "coverage": "Belfast, Sydenham",
            },
            "bt5": {
                "position": "east",
                "post_town": "Belfast",
                "coverage": "Belfast, Castlereagh, Crossnacreevy, Gilnahirk, Knock",
            },
            "bt6": {
                "position": "east",
                "post_town": "Belfast",
                "coverage": "Belfast, Castlereagh, Knockbreda",
            },
            "bt7": {
                "position": "south",
                "post_town": "Belfast",
                "coverage": "Belfast, Ormeau, Botanic, Holylands",
            },
            "bt8": {
                "position": "south",
                "post_town": "Belfast",
                "coverage": "Belfast, Carryduff, Knockbreda, Newtownbreda",
            },
            "bt9": {
                "position": "south",
                "post_town": "Belfast",
                "coverage": "Belfast, Malone, Lisburn Road, Taughmonagh, Stranmillis",
            },
            "bt10": {
                "position": "south",
                "post_town": "Belfast",
                "coverage": "Belfast, Finaghy",
            },
            "bt11": {
                "position": "west",
                "post_town": "Belfast",
                "coverage": "Belfast, Andersonstown, Lenadoon, Suffolk, Ladybrook, Turf Lodge",
            },
            "bt12": {
                "position": "south,west",
                "post_town": "Belfast",
                "coverage": "Belfast, Sandy Row, The Village. Falls Road",
            },
            "bt13": {
                "position": "north,west",
                "post_town": "Belfast",
                "coverage": "Belfast, Shankill Road, Woodvale, Ballygomartin, Springmartin, Glencairn, Highfield. Clonard",
            },
            "bt14": {
                "position": "north",
                "post_town": "Belfast",
                "coverage": "Belfast, Crumlin Road, Ballysillan, Upper Ballysillan, Ardoyne",
            },
            "bt15": {
                "position": "north",
                "post_town": "Belfast",
                "coverage": "Belfast, York Road, Antrim Road, New Lodge, Sailortown",
            },
            "bt16": {
                "position": "east",
                "post_town": "Belfast",
                "coverage": "Dundonald",
            },
            "bt17": {
                "position": "west,north",
                "post_town": "Belfast",
                "coverage": "Belfast, Dunmurry, Hannahstown, Twinbrook, Poleglass, Lagmore. Derriaghy, Seymour Hill",
            },
            "bt18": {
                "position": "east",
                "post_town": "Holywood",
                "coverage": "Holywood, Craigavad",
            },
            "bt19": {
                "position": "east",
                "post_town": "Bangor",
                "coverage": "Bangor, Crawfordsburn, Groomsport, Helens Bay",
            },
            "bt20": {"position": "east", "post_town": "Bangor", "coverage": "Bangor"},
            "bt21": {
                "position": "east",
                "post_town": "Donaghadee",
                "coverage": "Donaghadee",
            },
            "bt22": {
                "position": "east",
                "post_town": "Newtownards",
                "coverage": "Newtownards, Ardkeen, Ballyhalbert, Ballywalter, Carrowdore, Cloughey, Greyabbey, Kircubbin, Millisle, Portaferry, Portavogie",
            },
            "bt23": {
                "position": "east",
                "post_town": "Newtownards",
                "coverage": "Newtownards, Ballygowan, Comber, Conlig, Killinchy, Moneyrea",
            },
            "bt24": {
                "position": "south",
                "post_town": "Ballynahinch",
                "coverage": "Ballynahinch, Drumaness, Saintfield",
            },
            "bt25": {
                "position": "south",
                "post_town": "Dromore",
                "coverage": "Dromore, Dromara, Finnis, Waringsford. ",
            },
            "bt26": {
                "position": "south",
                "post_town": "Hillsborough",
                "coverage": "Hillsborough, Annahilt, Culcavy. ",
            },
            "bt27": {
                "position": "south-west",
                "post_town": "Lisburn",
                "coverage": "Lisburn, Cargacreevy, Drumalig, Drumbo, Hilden, Hillhall, Lambeg. ",
            },
            "bt28": {
                "position": "south-west",
                "post_town": "Lisburn",
                "coverage": "Lisburn, Ballinderry Lower, Ballinderry Upper, Stoneyford",
            },
            "bt29": {
                "position": "north",
                "post_town": "Belfast",
                "coverage": "Belfast, Crumlin, Aldergrove, Dundrod, Glenavy, Nutts Corner",
            },
            "bt30": {
                "position": "south-east",
                "Downpatrick": "Downpatrick, Ardglass, Ballyhornan, Ballykinler, Castleward, Clough, Crossgar, Kilclief, Killard, Killough, Killyleagh, Loughinisland, Seaforde, Strangford, Toye",
            },
            "bt58": {
                "position": "centre",
                "post_town": "Belfast",
                "coverage": "Belfast",
            },
            "bt99": {
                "position": "centre",
                "post_town": "Belfast",
                "coverage": "Belfast",
            },
        }

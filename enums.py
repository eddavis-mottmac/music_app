from enum import Enum

class States(Enum):
    ALABAMA = "AL"
    ALASKA = "AK"
    ARIZONA = "AZ"
    ARKANSAS = "AR"
    CALIFORNIA = "CA"
    COLORADO = "CO"
    CONNECTICUT = "CT"
    DELAWARE = "DE"
    FLORIDA = "FL"
    GEORGIA = "GA"
    HAWAII = "HI"
    IDAHO = "ID"
    ILLINOIS = "IL"
    INDIANA = "IN"
    IOWA = "IA"
    KANSAS = "KS"
    KENTUCKY = "KY"
    LOUISIANA = "LA"
    MAINE = "ME"
    MARYLAND = "MD"
    MASSACHUSETTS = "MA"
    MICHIGAN = "MI"
    MINNESOTA = "MN"
    MISSISSIPPI = "MS"
    MISSOURI = "MO"
    MONTANA = "MT"
    NEBRASKA = "NE"
    NEVADA = "NV"
    NEW_HAMPSHIRE = "NH"
    NEW_JERSEY = "NJ"
    NEW_MEXICO = "NM"
    NEW_YORK = "NY"
    NORTH_CAROLINA = "NC"
    NORTH_DAKOTA = "ND"
    OHIO = "OH"
    OKLAHOMA = "OK"
    OREGON = "OR"
    PENNSYLVANIA = "PA"
    RHODE_ISLAND = "RI"
    SOUTH_CAROLINA = "SC"
    SOUTH_DAKOTA = "SD"
    TENNESSEE = "TN"
    TEXAS = "TX"
    UTAH = "UT"
    VERMONT = "VT"
    VIRGINIA = "VA"
    WASHINGTON = "WA"
    WEST_VIRGINIA = "WV"
    WISCONSIN = "WI"
    WYOMING = "WY"


class Genres(Enum):
    ALTERNATIVE = "Alternative"
    BLUES = "Blues"
    CLASSICAL = "Classical"
    COUNTRY = "Country"
    ELECTRONIC = "Electronic"
    FOLK = "Folk"
    FUNK = "Funk"
    HIP_HOP = "Hip-Hop"
    HEAVY_METAL = "Heavy Metal"
    INSTRUMENTAL = "Instrumental"
    JAZZ = "Jazz"
    MUSICAL_THEATRE = "Musical Theatre"
    POP = "Pop"
    PUNK = "Punk"
    R_B = "R&B"
    REGGAE = "Reggae"
    ROCK_N_ROLL = "Rock n Roll"
    SOUL = "Soul"
    OTHER = "Other"


class StatesPhoneCodes(Enum):
    ALABAMA = ("AL", ["205", "251", "256", "334", "938"])
    ALASKA = ("AK", ["907"])
    ARIZONA = ("AZ", ["480", "520", "602", "623", "928"])
    ARKANSAS = ("AR", ["479", "501", "870"])
    CALIFORNIA = ("CA", ["209", "213", "310", "323", "408", "415", "424", "442", "510", "530", "559", "562", "619", "626", "650", "657", "661", "669", "707", "714", "747", "760", "805", "818", "831", "858", "909", "916", "925", "949", "951"])
    COLORADO = ("CO", ["303", "719", "720", "970"])
    CONNECTICUT = ("CT", ["203", "475", "860", "959"])
    DELAWARE = ("DE", ["302"])
    FLORIDA = ("FL", ["239", "305", "321", "352", "386", "407", "561", "727", "754", "772", "786", "813", "850", "863", "904", "941", "954"])
    GEORGIA = ("GA", ["229", "404", "470", "478", "678", "706", "770", "912"])
    HAWAII = ("HI", ["808"])
    IDAHO = ("ID", ["208"])
    ILLINOIS = ("IL", ["217", "224", "309", "312", "630", "708", "773", "815", "847", "872"])
    INDIANA = ("IN", ["219", "260", "317", "574", "765", "812", "930"])
    IOWA = ("IA", ["319", "515", "563", "641", "712"])
    KANSAS = ("KS", ["316", "620", "785", "913"])
    KENTUCKY = ("KY", ["270", "502", "606", "859"])
    LOUISIANA = ("LA", ["225", "318", "337", "504", "985"])
    MAINE = ("ME", ["207"])
    MARYLAND = ("MD", ["240", "301", "410", "443", "667"])
    MASSACHUSETTS = ("MA", ["339", "351", "413", "508", "617", "774", "781", "857", "978"])
    MICHIGAN = ("MI", ["231", "248", "269", "313", "517", "586", "616", "734", "810", "906", "947", "989"])
    MINNESOTA = ("MN", ["218", "320", "507", "612", "651", "763", "952"])
    MISSISSIPPI = ("MS", ["228", "601", "662", "769"])
    MISSOURI = ("MO", ["314", "417", "573", "636", "660", "816", "957"])
    MONTANA = ("MT", ["406"])
    NEBRASKA = ("NE", ["308", "402"])
    NEVADA = ("NV", ["702", "725", "775"])
    NEW_HAMPSHIRE = ("NH", ["603"])
    NEW_JERSEY = ("NJ", ["201", "551", "609", "732", "848", "856", "862", "908", "973"])
    NEW_MEXICO = ("NM", ["505", "575"])
    NEW_YORK = ("NY", ["212", "315", "347", "516", "518", "585", "607", "631", "646", "716", "718", "845", "914", "917", "929"])
    NORTH_CAROLINA = ("NC", ["252", "336", "704", "828", "910", "919", "980", "984"])
    NORTH_DAKOTA = ("ND", ["701"])
    OHIO = ("OH", ["216", "234", "330", "419", "440", "513", "614", "740", "937"])
    OKLAHOMA = ("OK", ["405", "539", "580", "918"])
    OREGON = ("OR", ["503", "541", "971"])
    PENNSYLVANIA = ("PA", ["215", "267", "272", "412", "484", "570", "610", "717", "724", "814", "878"])
    RHODE_ISLAND = ("RI", ["401"])
    SOUTH_CAROLINA = ("SC", ["803", "843", "864"])
    SOUTH_DAKOTA = ("SD", ["605"])
    TENNESSEE = ("TN", ["423", "615", "731", "865", "901", "931"])
    TEXAS = ("TX", ["210", "214", "254", "281", "325", "346", "361", "409", "432", "469", "512", "682", "713", "737", "806", "817", "830", "832", "903", "915", "940", "956", "972", "979"])
    UTAH = ("UT", ["385", "435", "801"])
    VERMONT = ("VT", ["802"])
    VIRGINIA = ("VA", ["276", "434", "540", "571", "703", "757", "804"])
    WASHINGTON = ("WA", ["206", "253", "360", "425", "509"])
    WEST_VIRGINIA = ("WV", ["304", "681"])
    WISCONSIN = ("WI", ["262", "414", "534", "608", "715", "920"])
    WYOMING = ("WY", ["307"])

    def __init__(self, abbreviation, codes):
        self.abbreviation = abbreviation
        self.codes = codes

    def is_valid_phone_number(self, phone_number):
        return any(phone_number.startswith(code) for code in self.codes)

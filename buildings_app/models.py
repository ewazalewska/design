from django.db import models

class Project(models.Model):
    # Available choices for TYPES_BUILDING field
    SFH = 'single family house'
    SDH = 'semi-detached house'
    IN = 'industry'
    RD = 'redecoration'
    OT = 'other type'

    # Available choices for TYPES_ELEVATION field
    TB = 'timber'
    PL = 'plaster'
    SS = 'steel sheet'
    ST = 'stone'

    # Available choices for TYPES_ROOF field
    FR = 'flat roof'
    OG = 'open gamble'
    HR = 'hipped roof'
    DM = 'dormer'

    # Available choices for TYPES_WALL and TYPES_CEILING fields
    RC = 'reinforced concrete'
    WD = 'wood'
    SB = 'steel beams'
    PB = 'prefabricated'
    BW = 'bricks'

    TYPES_BUILDING = [
        (SFH, 'single family house'),
        (SDH, 'semi-detached house'),
        (IN, 'industry'),
        (RD, 'redecoration'),
        (OT, 'other type'),
    ]

    symbol = models.CharField(max_length=6, blank=False, unique=True)               # Each project has unique name
    type = models.CharField(max_length=30, choices=TYPES_BUILDING, default=OT)

    # Details and parameters used in database and Django administration:
    investor_first_name = models.CharField(max_length=30, null=True, blank=True)
    investor_last_name = models.CharField(max_length=30, null=True, blank=True)
    date_of_the_order = models.DateField(null=True, blank=True)
    floors = models.PositiveSmallIntegerField(blank=True, default=0)
    area = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    TYPES_WALL = [
        (RC, 'reinforced concrete'),
        (WD, 'wood'),
        (SB, 'steel beams'),
        (PB, 'prefabricated'),
        (BW, 'bricks'),
        (OT, 'other type'),
    ]

    walls = models.CharField(max_length=30, choices=TYPES_WALL, default=OT)

    TYPES_CEILING = [
        (RC, 'reinforced concrete'),
        (WD, 'wood'),
        (SB, 'steel beams'),
        (PB, 'prefabricated'),
        (OT, 'other type'),
    ]

    ceiling = models.CharField(max_length=30, choices=TYPES_CEILING, default=OT)

    TYPES_ROOF = [
        (FR, 'flat roof'),
        (OG, 'open gamble'),
        (HR, 'hipped roof'),
        (DM, 'dormer'),
        (OT, 'other type'),
    ]

    roof = models.CharField(max_length=30, choices=TYPES_ROOF, default=OT)

    TYPES_ELEVATION = [
        (TB, 'timber'),
        (PL, 'plaster'),
        (SS, 'steel sheet'),
        (ST, 'stone'),
        (OT, 'other type'),
    ]

    elevation = models.CharField(max_length=30, choices=TYPES_ELEVATION, default=OT)
    view = models.ImageField(upload_to='views', null=True, blank=True)

    # Returns basic parameters of the object, shown at the main page
    def parameters(self):
        return "floors: {}, {} m2".format(self.floors, self.area)

    # Returns a description of technology which is shown at the main page
    def description(self):
        return "elevation: {}, " \
               "roof: {}, " \
               "ceiling: {}, " \
               "walls: {}".format(self.elevation, self.roof, self.ceiling, self.walls)

from django.db import models

class Project(models.Model):
    SFH = 'single family house'
    SDH = 'semi-detached house'
    IN = 'industry'
    RD = 'redecoration'
    OT = 'other type'

    TB = 'timber'
    PL = 'plaster'
    SS = 'steel sheet'
    ST = 'stone'

    FR = 'flat roof'
    OG = 'open gamble'
    HR = 'hipped roof'
    DM = 'dormer'

    RC = 'reinforced concrete'
    WD = 'wood'
    SB = 'steel beams'
    PB = 'prefabricated'
    BW = 'bricks'

    TYPES = [
        (SFH, 'single family house'),
        (SDH, 'semi-detached house'),
        (IN, 'industry'),
        (RD, 'redecoration'),
        (OT, 'other type'),
    ]

    symbol = models.CharField(max_length=6, blank=False, unique=True)
    type = models.CharField(max_length=30, choices=TYPES, default=OT)
    investor_first_name = models.CharField(max_length=30, null=True, blank=True)
    investor_last_name = models.CharField(max_length=30, null=True, blank=True)
    date_of_the_order = models.DateField(null=True, blank=True)
    floors = models.PositiveSmallIntegerField(blank=True, default=0)
    area = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    TYPES_W = [
        (RC, 'reinforced concrete'),
        (WD, 'wood'),
        (SB, 'steel beams'),
        (PB, 'prefabricated'),
        (BW, 'bricks'),
        (OT, 'other type'),
    ]

    walls = models.CharField(max_length=30, choices=TYPES_W, default=OT)

    TYPES_C = [
        (RC, 'reinforced concrete'),
        (WD, 'wood'),
        (SB, 'steel beams'),
        (PB, 'prefabricated'),
        (OT, 'other type'),
    ]

    ceiling = models.CharField(max_length=30, choices=TYPES_C, default=OT)

    TYPES_R = [
        (FR, 'flat roof'),
        (OG, 'open gamble'),
        (HR, 'hipped roof'),
        (DM, 'dormer'),
        (OT, 'other type'),
    ]

    roof = models.CharField(max_length=30, choices=TYPES_R, default=OT)

    TYPES_E = [
        (TB, 'timber'),
        (PL, 'plaster'),
        (SS, 'steel sheet'),
        (ST, 'stone'),
        (OT, 'other type'),
    ]

    elevation = models.CharField(max_length=30, choices=TYPES_E, default=OT)
    view = models.ImageField(upload_to='views', null=True, blank=True)

    def __str__(self):
        return self.symbol + ' - ' + self.type

    def parameters(self):
        return "floors: {}, {} m2".format(self.floors, self.area)

    def description(self):
        return "elevation: {}, " \
               "roof: {}, " \
               "ceiling: {}, " \
               "walls: {}".format(self.elevation, self.roof, self.ceiling, self.walls)






from django.db import models

import json
import urllib.request

class USTContract(models.Model):
    evepraisalURL = models.URLField()
    totalSize = models.FloatField(default=0)
    collateral = models.FloatField(default=0)
    reward = models.FloatField(default=0)
    evepraisalID = models.CharField(max_length=6)
    rush = models.BooleanField()

    def getData(self):
        url = self.evepraisalURL + ".json"
        response = urllib.request.urlopen(url)
        str_response = response.read().decode('utf-8')
        data = json.loads(str_response)
        self.evepraisalID = data["id"]
        self.totalSize = data["totals"]["volume"]
        self.collateral= data["totals"]["buy"]

        if self.rush == 0:
            if self.collateral > 100000000:
                self.reward = (self.totalSize * 750) + (self.collateral * 0.05)
            else:
                self.reward = (self.totalSize * 750)

            if self.reward < 10000000:
                self.reward = 10000000

            if self.totalSize <= 100 and self.collateral < 100000000:
                self.reward = 0
        else:
            self.reward = 200000000 + (self.collateral * 0.05)
        
    def __str__(self):
        return self.evepraisalURL


class USTResult(models.Model):
    contract = models.ForeignKey(USTContract, on_delete=models.CASCADE)

    def __str__(self):
        return self.contract

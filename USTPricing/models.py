from django.db import models

import json
import urllib.request


class USTContract(models.Model):
    evepraisalURL = models.URLField()
    totalSize = models.FloatField(default=0)
    collateral = models.FloatField(default=0)
    reward = models.FloatField(default=0)
    evepraisalID = models.CharField(max_length=6)
    rush = models.BooleanField(default=False)
    altloc = models.BooleanField(default=False)
    contractExpiration = models.IntegerField(default=0)
    deliveryTime = models.IntegerField(default=0)

    def getData(self):
        url = self.evepraisalURL + ".json"
        response = urllib.request.urlopen(url)
        str_response = response.read().decode('utf-8')
        data = json.loads(str_response)
        self.evepraisalID = data["id"]
        self.totalSize = data["totals"]["volume"]
        self.collateral = data["totals"]["buy"]

        iskperm3 = 500
        altiskperm3 = 1000

        print(self.rush)
        print(self.altloc)

        if (self.rush is False) and (self.altloc is False):
            self.contractExpiration = 14
            self.deliveryTime = 14

            if self.totalSize <= 500 and self.collateral < 100000000:
                self.reward = 0
            else:
                if self.collateral > 100000000:
                    self.reward = (self.totalSize * iskperm3) + (self.collateral * 0.05)
                else:
                    self.reward = (self.totalSize * iskperm3)

                if self.reward < 15000000:
                    self.reward = 15000000 + (self.collateral * 0.05)

                if 100 <= self.totalSize < 15000 and self.reward < 5000000:
                    self.reward = 5000000 + (self.collateral * 0.05)
        elif (self.rush is False) and (self.altloc is True):
            self.contractExpiration = 28
            self.deliveryTime = 28
            print(self.contractExpiration)
            print(self.deliveryTime)
            if self.totalSize <= 100 and self.collateral < 100000000:
                self.reward = 0
            else:
                if self.collateral > 100000000:
                    self.reward = (self.totalSize * altiskperm3) + (self.collateral * 0.05)
                else:
                    self.reward = (self.totalSize * altiskperm3)

                if self.reward < 15000000:
                    self.reward = 15000000 + (self.collateral * 0.05)

                if 100 <= self.totalSize < 15000 and self.reward < 5000000:
                    self.reward = 5000000 + (self.collateral * 0.05)

        elif self.rush is True and self.altloc is False:
            self.contractExpiration = 14
            self.deliveryTime = 14
            self.reward = 600000000 + (self.collateral * 0.05)
        elif self.rush is True and self.altloc is True:
            self.contractExpiration = 28
            self.deliveryTime = 28
            self.reward = 750000000 + (self.collateral * 0.05)
        
    def __str__(self):
        return self.evepraisalURL


class USTResult(models.Model):
    contract = models.ForeignKey(USTContract, on_delete=models.CASCADE)

    def __str__(self):
        return self.contract

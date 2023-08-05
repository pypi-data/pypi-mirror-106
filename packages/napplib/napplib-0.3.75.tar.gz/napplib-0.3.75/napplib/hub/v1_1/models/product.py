import sys, datetime
sys.path.append("..")
from ..utils import Utils

class InventoryList:
    def __init__(self, sku='',
                        listPrice='',
                        salePrice='',
                        stockQuantity='',
    ):
        self.sku = sku
        self.listPrice = listPrice if listPrice else 0
        self.salePrice = salePrice if salePrice else 0
        self.stockQuantity = stockQuantity if stockQuantity else 0

class StoreProductMarketplaceFieldUpdate:
    id: int
    statusProcessing: str
    marketplaceForeignId: str
    mktPartnerProductId: int

    def __init__(self, id: int,
                        statusProcessing: str = None,
                        marketplaceForeignId: str = None,
                        mktPartnerProductId: int = None) -> None:
        self.id = id
        if statusProcessing:
            self.statusProcessing = statusProcessing
        if marketplaceForeignId:
            self.marketplaceForeignId = marketplaceForeignId
        if mktPartnerProductId:
            self.mktPartnerProductId = mktPartnerProductId

class Product:
    def __init__(self,  id='',
                        parentSku='',
                        sku='',
                        ean='',
                        name='',
                        description='',
                        brandName='',
                        categoryName='',
                        warrantyTime='',
                        listPrice='',
                        salePrice='',
                        stockQuantity='',
                        weight='',
                        width='',
                        length='',
                        height='',
                        active=None,
                        attributes=[],
                        images=[]):
        self.id = id if id else None
        self.parentSku = parentSku if parentSku else None
        self.sku = sku
        self.ean = ean
        self.name = name
        self.description = description
        self.categoryName = categoryName
        self.brandName = brandName if brandName else None
        self.warrantyTime = warrantyTime if warrantyTime else 0
        self.listPrice = listPrice if listPrice else 0
        self.salePrice = salePrice if salePrice else 0
        self.stockQuantity = stockQuantity if stockQuantity else 0
        self.weight = weight if weight else 1
        self.width = width if width else 1
        self.length = length if length else 1
        self.height = height if height else 1
        self.active = active
        self.attributes = attributes
        self.images = images

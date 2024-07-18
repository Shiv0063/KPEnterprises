from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('CallEntry',views.CallEntry,name="Call Entry"),
    path('DeleteCallEntry/<int:id>',views.DeleteCallEntry,name="Call Entry Delete"),
    path('PartyName/<str:PN>',views.PartyName,name="Party Name"),
    path('Citys',views.Citys,name="Citys"),
    path('Branch/<str:City>',views.Branch,name="Branch"),
    path('EntryClase',views.EntryClase,name="Call Entry Clase"),
    path('RCCreat',views.RCCreat,name="RC Creat"),
    path('RCEdit',views.RCEdit,name="RC Edit"),
    path('RCDelete',views.RCDelete,name="RC Delete"),
    path('AddCallEntry',views.AddCallEntry,name="Add Call Entry"),
    path('EditCallEntry/<int:pk>',views.EditCallEntry,name="Edit Call Entry"),
    path('PendingCall',views.PendingCall,name="Pending Call"),
    path('PendingWorkOrder',views.PendingWorkOrder,name="Pending WorkOrder"),
    path('Cluster',views.Cluster,name="Cluster"),
    path('EditCluster/<int:id>',views.EditCluster,name="Edit Cluster"),
    path('DeleteCluster/<int:id>',views.DeleteCluster,name="Delete Cluster"),
    path('CostCode',views.CostCode,name="Cost Code"),
    path('EditCostCode/<int:id>',views.EditCostCode,name="Edit Cost Code"),
    path('DeleteCostCode/<int:id>',views.DeleteCostCode,name="Delete Cost Code"),
    path('GST',views.GST,name="GST"),
    path('PartyName',views.PartyName,name="Party Name"),
    path('EditPartyName/<int:id>',views.EditPartyName,name="Edit Party Name"),
    path('DeletePartyName/<int:id>',views.DeletePartyName,name="Delete Party Name"),
    path('EditGST/<int:id>',views.EditGST,name="Edit GST"),
    path('DeleteGST/<int:id>',views.DeleteGST,name="Delete GST"),
    path('Party',views.Party,name="party"),
    path('AddParty',views.AddParty,name="Add party"),
    path('EditParty/<int:id>',views.EditParty,name="Edit Party"),
    path('DeleteParty/<int:id>',views.DeleteParty,name="Delete Party"),
    path('Labour',views.Labour,name="Labour"),
    path('EditLabour/<int:id>',views.EditLabour,name="Edit Labour"),
    path('DeleteLabour/<int:id>',views.DeleteLabour,name="Delete Labour"),
    path('AddLabour',views.AddLabour,name="Add Labour"),
    path('RCCode',views.Rate,name="Rate"),
    path('AddRate',views.AddRate,name="Add Rate"),
    path('EditRate/<int:id>',views.EditRate,name="Edit Rate"),
    path('DeleteRate/<int:id>',views.DeleteRate,name="Delete Rate"),
    path('Invoice',views.Invoice,name="Invoice"),
    path('AddInvoice',views.AddInvoice,name="Add Invoice"),
    path('AddInvoiceMaIN',views.AddInvoiceMaIN,name="Add Invoice Main Form"),
    path('RCCODE',views.RCCODE,name="RCCODE"),
    path('CompleteCall',views.CompleteCall,name="Complete Call"),
    path('Quotation',views.QuotationEntry,name="Quotation Entry"),
    path('DeleteQuotation/<int:id>',views.DeleteQuotation,name="Quotation delete"),
    path('EditQuotation/<int:id>',views.EditQuotation,name="Quotation Edit"),
    path('QuotationP/<int:id>',views.QuotationP,name="Quotation Print"),
    path('AddQuotation',views.AddQuotation,name="Add Quotation"),
    path('QRCCreat',views.QRCCreat,name="QRC Creat"),
    path('QRCEdit',views.QRCEdit,name="QRC Edit"),
    path('QRCDelete',views.QRCDelete,name="QRC Delete"),
    path('CodeNoC',views.CodeNoC,name="CodeNoC"),
    path('PartyData',views.PartyData,name="PartyData"),
    path('ClaseQuotation/<int:id>',views.ClaseQuotation,name="Clase Quotation"),
    path('TaxInvoice/<int:id>',views.TaxInvoice,name="Tax Invoice"),
    path('ETOE/<int:id>',views.export_to_excel,name="Export To Excel_A"),
    path('HSN/<int:id>',views.HSN,name="Export To Excel_HSN"),
    path('SoftCopy/<int:id>',views.SoftCopy,name="Export To SoftCopy"),
    path('CCName',views.CCName,name='CCName'),
    path('ClusterReport',views.Annexure,name='ClusterReport'),
    path('ClusterEL',views.ClusterEL,name='ClusterEL'),
    path('login',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

package routes

import (
	controller "golang-GESTION-Hotel/controllers"

	"github.com/gin-gonic/gin"
)

func InvoiceRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.GET("/invoices", controller.GetInvoices()) //renvoie toutes les factures

	incomingRoutes.GET("/invoices/:invoice_id", controller.GetInvoice()) //renvoie une facture spécifique

	incomingRoutes.POST("/invoices", controller.CreateInvoice()) //crée une nouvelle facture

	incomingRoutes.PATCH("/invoices/:invoice_id", controller.UpdateInvoice()) //met à jour une facture
}

package routes

import (
	controller "golang-GESTION-Hotel/controllers"

	"github.com/gin-gonic/gin"
)

func TableRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.GET("/tables", controller.GetTables()) //renvoie toutes les réservations de l'application.

	incomingRoutes.GET("/tables/:table_id", controller.GetTable()) // renvoie les détails de la réservation

	incomingRoutes.POST("/tables", controller.CreateTable()) //créer une nouvelle réservation dans l'application

	incomingRoutes.PATCH("/tables/:table_id", controller.UpdateTable()) //mettre à jour les détails d'une réservation existante
}

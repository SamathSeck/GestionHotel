package routes

import (
	controller "golang-GESTION-Hotel/controllers"

	"github.com/gin-gonic/gin"
)

func OrderItemRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.GET("/orderItems", controller.GetOrderItems()) //renvoie tous les éléments des service annexes de l'application.

	incomingRoutes.GET("/orderItems/:orderItem_id", controller.GetOrderItem()) // créer une nouvel service

	incomingRoutes.GET("/orderItems-order/:order_id", controller.GetOrderItemByOrder()) //renvoie touts les éléments de service associés à la servicee spécifiée

	incomingRoutes.POST("/orderItems", controller.CreateOrderItem()) //créer une service

	incomingRoutes.PATCH("/orderItems/:orderItem_id", controller.UpdateOrderItem()) //mettre à jour les détails
}

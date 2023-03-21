package routes

import (
	controller "golang-GESTION-Hotel/controllers"

	"github.com/gin-gonic/gin"
)

func MenuRoutes(incomingRoutes *gin.Engine) {
	incomingRoutes.GET("/menus", controller.GetMenus())              // renvoie tous les chambres de l'application.
	incomingRoutes.GET("/menus/:menu_id", controller.GetMenu())      //renvoie les détails de la chambre
	incomingRoutes.POST("/menus", controller.CreateMenu())           //créer une chambre
	incomingRoutes.PATCH("/menus/:menu_id", controller.UpdateMenu()) //mettre à jour les détails
}

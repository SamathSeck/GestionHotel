package main

import (
	"golang-GESTION-Hotel/database"
	middleware "golang-GESTION-Hotel/middleware"
	routes "golang-GESTION-Hotel/routes"
	"os"

	"github.com/gin-gonic/gin"
	"go.mongodb.org/mongo-driver/mongo"
)

/*base de donne attendre mor talla ou mysql
//proxysql.com/ */

var foodCollection *mongo.Collection = database.OpenCollection(database.Client, "food")

func main() {
	port := os.Getenv("port")

	if port == "" {
		port = "8008"
	}
	router := gin.New()
	router.Use(gin.Logger())
	routes.UserRoutes(router)
	router.Use(middleware.Authentication())

	routes.FoodRoutes(router)      //Hotel *in my mind
	routes.MenuRoutes(router)      //Chambre --
	routes.TableRoutes(router)     //reservation --
	routes.OrdersRoutes(router)    //
	routes.OrderItemRoutes(router) //services annexes --
	routes.InvoiceRoutes(router)   // facture *in english

	router.Run(":" + port)
}

/*api realisée avec une base de données MongoDB capabable de se connecter une base de données
proxySQL mais cela nécessite la mise en place d'un système d'agrégation de données entre les deux technologies.
*/

/* ce code implémente une API pour une application de gestion d'hôtel qui permet à l'utilisateur de consulter et de gérer les chambres, les réservations, les services annexes et les factures.

 */

from flask import Flask, render_template
app = Flask(__name__)

cocktailList = [{"Name":"Alexander","Alcohol":"Cognac","Ingredients":"3 cl cognac, 3 cl white creme de cacao, 3 cl light cream"},
{"Name":"Americano","Alcohol":"Vermouth","Ingredients":"3 cl Campari, 3 cl red vermouth, A splash of soda water"},
{"Name":"Aviation","Alcohol":"Gin","Ingredients":"4.5 cl gin, 1.5 cl lemon juice, 1.5 cl maraschino liqueur"},
{"Name":"Bacardi Cocktail","Alcohol":"Rum","Ingredients":"4.5 cl white rum, 2 cl lime juice, 1 cl grenadine syrup"},
{"Name":"Casino","Alcohol":"Gin","Ingredients":"4 cl gin (Old Tom), 1 cl Maraschino, 1 cl orange bitters, 1 cl fresh lemon juice"},
{"Name":"Clover Club Cocktail","Alcohol":"Gin","Ingredients":"4.5cl Gin, 1.5cl Lemon Juice, 1.5cl Raspberry Syrup, 1 Egg White"},
{"Name":"Daiquiri","Alcohol":"Rum","Ingredients":"4.5 cl (9 parts) white rum, 2.5 cl (5 parts) lime juice, 1.5 cl (3 parts) simple syrup"},
{"Name":"Martini","Alcohol":"Gin","Ingredients":"6 cl (6 parts) gin, 1 cl (1 parts) dry vermouth"},
{"Name":"Manhattan","Alcohol":"Whiskey","Ingredients":"5 cL rye, 2 cL Sweet red vermouth, Dash Angostura bitters"},
{"Name":"Negroni","Alcohol":"Gin","Ingredients":"3 cl gin, 3 cl sweet red vermouth, 3 cl campari"},
{"Name":"Old Fashioned","Alcohol":"Whiskey","Ingredients":"4.5 cL Bourbon or Rye whiskey, 2 dashes Angostura bitters, 1 sugar cube, Few dashes plain water"},
{"Name":"Paradise","Alcohol":"Gin","Ingredients":"3.5 cl (7 parts) gin, 2 cl (4 parts) apricot brandy, 1.5 cl (3 parts) orange juice"},
{"Name":"Planter's Punch","Alcohol":"Rum","Ingredients":"4.5cl Dark rum, 3.5 cl Fresh orange juice, 3.5 cl Fresh pineapple juice, 2 cl Fresh lemon juice, 1 cl Grenadine syrup, 1 cl Sugar syrup, 3 or 4 dashes Angostura bitters"},
{"Name":"Porto flip","Alcohol":"Port","Ingredients":"1.5 cl (3 parts) brandy, 4 cl (8 parts) port, 1 cl (2 parts) egg yolk"},
{"Name":"Rusty Nail","Alcohol":"Scotch whisky","Ingredients":"7.5 cl Scotch Whisky, 2.5 cl Drambuie"},
{"Name":"Sazerac","Alcohol":"Cognac","Ingredients":"5 cl Cognac, 1 cl Absinthe, One sugar cube, Two dashes Peychaud's Bitters"},
{"Name":"Screwdriver","Alcohol":"Vodka","Ingredients":"5 cL (1 part) vodka, 10 cL (2 parts) orange juice"},
{"Name":"Whiskey sour","Alcohol":"Whiskey","Ingredients":"4.5 cl (3 parts) Bourbon whiskey, 3 cl (2 parts) fresh lemon juice, 1.5 cl (1 part) Gomme syrup, dash egg white (optional)"},
{"Name":"Bellini","Alcohol":"Prosecco","Ingredients":"10 cl (2 parts) Prosecco, 5 cl (1 part) fresh peach puree"},
{"Name":"Black Russian","Alcohol":"Vodka","Ingredients":"5 cl (5 parts) Vodka, 2 cl (2 parts) Coffee liqueur"},
{"Name":"Bloody Mary","Alcohol":"Vodka","Ingredients":"4.5 cl (3 parts) Vodka, 9 cl (6 parts) Tomato juice, 1.5 cl (1 part) Lemon juice, 2 to 3 dashes of Worcestershire Sauce, Tabasco, Celery salt, Pepper"},
{"Name":"Caipirinha","Alcohol":"Cachacoa","Ingredients":"5 cl Cachacoa, Half a lime cut into 4 wedges, 2 teaspoons sugar"},
{"Name":"Cosmopolitan","Alcohol":"Vodka","Ingredients":"4 cl Vodka Citron, 1.5 cl Cointreau, 1.5 cl Fresh lime juice, 3 cl Cranberry juice"},
{"Name":"Cuba Libre","Alcohol":"Rum","Ingredients":"12 cL Cola, 5 cL Light rum, 1 cL Fresh lime juice"},
{"Name":"Godfather","Alcohol":"Scotch whisky","Ingredients":"3.5cl scotch whisky, 3.5cl Disaronno"},
{"Name":"Golden dream","Alcohol":"Orange-flavored liqueur","Ingredients":"2 cl (2 parts) Galliano, 2 cl (2 parts) Triple Sec, 2 cl (2 parts) Fresh orange juice, 1 cl (1 part) Fresh cream"},
{"Name":"Harvey Wallbanger","Alcohol":"Vodka","Ingredients":"4.5 cL (3 parts) Vodka, 1.5 cL (1 part) Galliano, 9 cL (6 parts) fresh orange juice"},
{"Name":"Horse's Neck","Alcohol":"Brandy","Ingredients":"4 cL (1 part) Brandy, 12 cL (3 parts) Ginger ale, Dash of Angostura bitter (optional)"},
{"Name":"Irish coffee","Alcohol":"Irish whiskey","Ingredients":"4 cl (2 parts) Irish whiskey, 8 cl (4 parts) hot coffee, 3 cl (1 1/2 parts) fresh cream, 1tsp brown sugar"},
{"Name":"Long Island Iced Tea","Alcohol":"Gin","Ingredients":"1.5 cl Tequila, 1.5 cl Vodka, 1.5 cl White rum, 1.5 cl Triple sec, 1.5 cl Gin, 2.5 cl Lemon juice, 3.0 cl Gomme Syrup, 1 dash of Cola"},
{"Name":"Mai Tai","Alcohol":"Rum","Ingredients":"4 cl white rum, 2 cl dark rum, 1.5 cl orange curacao, 1.5 cl Orgeat syrup, 1 cl fresh lime juice"},
{"Name":"Margarita","Alcohol":"Tequila","Ingredients":"3.5 cL (7 parts) tequila, 2 cL (4 parts) Cointreau, 1.5 cL (3 parts) lime juice"},
{"Name":"Mimosa","Alcohol":"Champagne","Ingredients":"7.5 cl champagne, 7.5 cl orange juice"},
{"Name":"Mint julep","Alcohol":"Bourbon whiskey","Ingredients":"6 cL Bourbon whiskey, 4 mint leaves, 1 teaspoon powdered sugar, 2 teaspoons water"},
{"Name":"Moscow mule","Alcohol":"Vodka","Ingredients":"4.5cl (9 parts) vodka, 0.5cl (1 part) lime juice, 12cl (24 parts) ginger beer"},
{"Name":"Pina colada","Alcohol":"Rum","Ingredients":"3 cl (one part) white rum, 3 cl (one part) coconut milk, 9 cl (3 parts) pineapple juice"},
{"Name":"Rose","Alcohol":"Vermouth","Ingredients":"4 cl (2 parts) dry vermouth, 2 cl (1 parts) Kirsch, 3 Dashes Strawberry syrup"},
{"Name":"Sea Breeze","Alcohol":"Vodka","Ingredients":"4 cl Vodka, 12 cl Cranberry juice, 3 cl Grapefruit juice"},
{"Name":"Sex on the Beach","Alcohol":"Vodka","Ingredients":"4 cl Vodka, 2 cl Peach schnapps, 4 cl Orange juice, 4 cl Cranberry juice"},
{"Name":"Singapore Sling","Alcohol":"Gin","Ingredients":"3 cl Gin, 1.5 cl Cherry Liqueur (cherry brandy), 0.75 cl Cointreau, 0.75 cl DOM Baonadictine, 1 cl Grenadine, 12 cl Pineapple juice, 1.5 cl Fresh lime juice, 1 dash Angostura bitters"},
{"Name":"Tequila Sunrise","Alcohol":"Tequila","Ingredients":"4.5 cl (3 parts) Tequila, 9 cl (6 parts) Orange juice, 1.5 cl (1 part) Grenadine syrup"},
{"Name":"Bramble","Alcohol":"Gin","Ingredients":"4 cl gin, 1.5 cl lemon juice, 1 cl simple syrup, 1.5 cl Creme de Mure(blackberry liqueur)"},
{"Name":"B-52","Alcohol":"Coffee liqueur","Ingredients":"\n2 cl (1 part) coffee liqueur (Kahlua), 2 cl (1 part) Irish Cream (Baileys Irish Cream), 2 cl (1 part) Orange Cognac (Grand Marnier)"},
{"Name":"Dark 'N' Stormy","Alcohol":"Rum","Ingredients":"\n6 cl dark rum, 10 cl Ginger beer"},
{"Name":"Martini","Alcohol":"Gin","Ingredients":"\n6 cl (6 parts) gin, 1 cl (1 parts) dry vermouth"},
{"Name":"Espresso Martini","Alcohol":"Vodka","Ingredients":"\n5 cl Vodka, 1 cl Kahlua, Sugar syrup (according to individual preference of sweetness), 1 short strong Espresso"},
{"Name":"Kamikaze","Alcohol":"Vodka","Ingredients":"3 cl vodka, 3 cl triple sec, 3 cl lime juice"},
{"Name":"Pisco sour","Alcohol":"Pisco","Ingredients":"4.5cl Pisco, 3cl lemon juice [a], 2cl Simple syrup, 1 Egg white[b]"},
{"Name":"Spritz","Alcohol":"Prosecco","Ingredients":"6cl Prosecco, 4cl Aperol, Splash of Soda water"},
{"Name":"Vesper","Alcohol":"Gin","Ingredients":"6cl gin, 1.5cl vodka, 0.75cl Lillet Blonde"}];

#here, I am getting the data from the dictionary and putting each row in a list because that is more manageable.
def get_names(data):
    names = []
    for row in data:
        name = row["Name"]
        names.append(name)
    return (names)

def get_drink_info(data, name):
    for row in data:
        if name == row["Name"]:
            alcohol = row["Alcohol"]
            ingredients = row["Ingredients"]
    return name, alcohol, ingredients

names = get_names(cocktailList)
#now my data should be easier to deal with

@app.route('/')
def home():
	return render_template('main.html', names=names)
    #this is the homepage

@app.route('/drink/<name>')
def drinks(name):
    name, alcohol, ingredients = get_drink_info(cocktailList, name)#this line of code has changed my life
    return render_template('drink.html', name=name, alcohol=alcohol, ingredients=ingredients)
    #this is each drink page
    
if __name__ == '__main__':
	app.run(debug=True)

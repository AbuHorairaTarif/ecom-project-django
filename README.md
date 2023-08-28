## Features

  **Product List:** Users can view a list of available products.
  **Product Search:** Users can search product from product list
  **Product Detail View:**: Users can view detail information about a specific product.
  **Product Review:** Users can submit reviews for products, including a rating with comments.
  **DIY Principal:** Navbar and footer section is common which is binded using Django template engine.


## Requirements:
- Python3 
- Pip 

## How to run the program:

**1. Clone this repo:** 

```bash
git clone https://github.com/AbuHorairaTarif/ecom-project-django.git
cd ecom-project-django
```

**2. Create and activate virtual environment:**

Go to project folder where `ecomenv` exist, then run terminal and type: `'source ecomenv/bin/activate'`

**3. Install Required Dependencies:**
After activating virtual environment install the following libraries:
```bash
pip install django
pip install django-autocomplete-light
pip install psycopg2-binary
pip install pillow
```

**4. PostgreSQL setup:**
```bash
cd postgres-test
docker-compose up -d
```

Go to browser: `localhost:8080` (if your system is using this port, update docker-compose.yml and change ports of pgadmin to different one
               email:admin@example.com
               password: adminpassword
               
**PGAdmin Setup:**               
After you login, pgadmin will ask for postgres password, then provide it:
After that, right click on `Server > Register > Server` in left sidemenu. In general tab give type any name you want as Server name. 
In connection tab give Host name: postgres, Username: myuser, Password: mypassword and save it.
Now create a database right clicking on your server name and named it mydatabase as I have mentioned in source code.
               (I have updated database instruction on my Django settings.py file, if you use different database name then update settings.py file)
               POSTGRES DB: mydatabase
               POSTGRES USER: myuser
               POSTGRES PASSWORD: mypassword
	
**Run Instruction in Terminal:**
On project directory, goto mysite where manage.py file exist, there you have to run terminal and type following commands:

`python3 manage.py migrate`
`python3 manage.py createsuperuser`
Superadmin (DJango Dashboard): (For example)
                User: **** (your username)
                email: ****
                Pass: **** (your pass)

**Run Server:**                
`python3 manage.py runserver 8082` (I have used different port to avoid port conflicts)
open the browser and goto
        `localhost:8082/admin` (type superadmin username and password)
                -You can add category, products and even update and delete comments of users.
        `localhost:8082/products`
                -There, you will find products that you have added on admin panel

 
In the mysite/media/products, you will find some sample image for testing or you can download from online.


# API Routes Outline

## Users

### Create User
- **POST /api/users**
  - Description: Creates a new user.
  - Request Body:
    - `username` (string): The username of the user.
    - `email` (string): The email of the user.
    - `password` (string): The password of the user.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Get User
- **GET /api/users/:id**
  - Description: Retrieves details of a specific user by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "User not found"
      }
      ```

### Update User
- **PUT /api/users/:id**
  - Description: Updates details of a specific user by ID.
  - Request Body:
    - `username` (string): The new username of the user.
    - `email` (string): The new email of the user.
    - `password` (string): The new password of the user.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "username": "new_user1",
        "email": "new_user1@example.com",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-20T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "User not found"
      }
      ```

### Delete User
- **DELETE /api/users/:id**
  - Description: Deletes a specific user by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "User deleted successfully"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "User not found"
      }
      ```

### Get All Users
- **GET /api/users**
  - Description: Retrieves a list of all users.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "username": "user1",
          "email": "user1@example.com",
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        },
        {
          "id": 2,
          "username": "user2",
          "email": "user2@example.com",
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        }
      ]
      ```

## Portfolios

### Create Portfolio
- **POST /api/portfolios**
  - Description: Creates a new portfolio.
  - Request Body:
    - `name` (string): The name of the portfolio.
    - `initial_balance` (number): The initial balance of the portfolio.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "Tech Stocks",
        "initial_balance": 10000.00,
        "current_value": 10000.00,
        "profit_loss": 0.00,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Get Portfolio
- **GET /api/portfolios/:id**
  - Description: Retrieves details of a specific portfolio by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "Tech Stocks",
        "initial_balance": 10000.00,
        "current_value": 10500.00,
        "profit_loss": 500.00,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-20T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Portfolio not found"
      }
      ```

### Get All Portfolios
- **GET /api/portfolios**
  - Description: Retrieves a list of all portfolios.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "user_id": 1,
          "name": "Tech Stocks",
          "initial_balance": 10000.00,
          "current_value": 10500.00,
          "profit_loss": 500.00,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-20T00:00:00"
        },
        {
          "id": 2,
          "user_id": 2,
          "name": "Growth Stocks",
          "initial_balance": 15000.00,
          "current_value": 15500.00,
          "profit_loss": 500.00,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-20T00:00:00"
        }
      ]
      ```

### Update Portfolio
- **PUT /api/portfolios/:id**
  - Description: Updates details of a specific portfolio by ID.
  - Request Body:
    - `name` (string): The new name of the portfolio.
    - `initial_balance` (number): The new initial balance of the portfolio.
    - `current_value` (number): The new current value of the portfolio.
    - `profit_loss` (number): The new profit/loss of the portfolio.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "Updated Tech Stocks",
        "initial_balance": 10000.00,
        "current_value": 10500.00,
        "profit_loss": 500.00,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-20T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Portfolio not found"
      }
      ```

### Delete Portfolio
- **DELETE /api/portfolios/:id**
  - Description: Deletes a specific portfolio by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "Portfolio deleted successfully"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Portfolio not found"
      }
      ```

## Portfolio Stocks

### Add Stock to Portfolio
- **POST /api/portfolios/:portfolio_id/stocks**
  - Description: Adds a stock to a specific portfolio.
  - Request Body:
    - `stock_id` (integer): The ID of the stock.
    - `quantity` (integer): The quantity of the stock.
    - `purchase_price` (number): The purchase price of the stock.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "portfolio_id": 1,
        "stock_id": 1,
        "quantity": 10,
        "purchase_price": 150.00,
        "current_price": 150.00,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Get Portfolio Stocks
- **GET /api/portfolios/:portfolio_id/stocks**
  - Description: Retrieves all stocks in a specific portfolio.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "portfolio_id": 1,
          "stock_id": 1,
          "quantity": 10,
          "purchase_price": 150.00,
          "current_price": 150.00,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        },
        {
          "id": 2,
          "portfolio_id": 1,
          "stock_id": 2,
          "quantity": 5,
          "purchase_price": 2800.00,
          "current_price": 2800.00,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        }
      ]
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Portfolio not found"
      }
      ```

### Update Portfolio Stock
- **PUT /api/portfolios/:portfolio_id/stocks/:id**
  - Description: Updates details of a specific stock in a portfolio.
  - Request Body:
    - `quantity` (integer): The new quantity of the stock.
    - `purchase_price` (number): The new purchase price of the stock.
    - `current_price` (number): The new current price of the stock.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "portfolio_id": 1,
        "stock_id": 1,
        "quantity": 20,
        "purchase_price": 150.00,
        "current_price": 150.00,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-20T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Portfolio or stock not found"
      }
      ```

### Delete Portfolio Stock
- **DELETE /api/portfolios/:portfolio_id/stocks/:id**
  - Description: Deletes a specific stock from a portfolio.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "Stock deleted from portfolio successfully"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Portfolio or stock not found"
      }
      ```

## Stocks

### Get Stock
- **GET /api/stocks/:id**
  - Description: Retrieves details of a specific stock by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "symbol": "AAPL",
        "name": "Apple Inc.",
        "current_price": 150.00,
        "market_cap": 2500000000,
        "pe_ratio": 30,
        "dividend_yield": 0.005,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Stock not found"
      }
      ```

## Stock Historical Prices

### Get Historical Prices
- **GET /api/stocks/:stock_id/historical_prices**
  - Description: Retrieves historical price data for a specific stock.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "stock_id": 1,
          "date": "2023-01-01",
          "open_price": 145.00,
          "close_price": 150.00,
          "high_price": 152.00,
          "low_price": 144.00,
          "volume": 100000
        },
        {
          "id": 2,
          "stock_id": 1,
          "date": "2023-01-02",
          "open_price": 150.00,
          "close_price": 151.00,
          "high_price": 153.00,
          "low_price": 149.00,
          "volume": 120000
        }
      ]
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Stock or historical prices not found"
      }
      ```

## Watchlists

### Create Watchlist
- **POST /api/watchlists**
  - Description: Creates a new watchlist.
  - Request Body:
    - `name` (string): The name of the watchlist.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "My Watchlist",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Get Watchlist
- **GET /api/watchlists/:id**
  - Description: Retrieves details of a specific watchlist by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "My Watchlist",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Watchlist not found"
      }
      ```

### Get All Watchlists
- **GET /api/watchlists**
  - Description: Retrieves a list of all watchlists.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "user_id": 1,
          "name": "My Watchlist",
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        },
        {
          "id": 2,
          "user_id": 2,
          "name": "Growth Watchlist",
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        }
      ]
      ```

### Update Watchlist
- **PUT /api/watchlists/:id**
  - Description: Updates details of a specific watchlist by ID.
  - Request Body:
    - `name` (string): The new name of the watchlist.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "Updated Watchlist",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-20T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Watchlist not found"
      }
      ```

### Delete Watchlist
- **DELETE /api/watchlists/:id**
  - Description: Deletes a specific watchlist by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "Watchlist deleted successfully"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Watchlist not found"
      }
      ```

## Watchlist Stocks

### Add Stock to Watchlist
- **POST /api/watchlists/:watchlist_id/stocks**
  - Description: Adds a stock to a specific watchlist.
  - Request Body:
    - `stock_id` (integer): The ID of the stock.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "watchlist_id": 1,
        "stock_id": 1,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Get Watchlist Stocks
- **GET /api/watchlists/:watchlist_id/stocks**
  - Description: Retrieves all stocks in a specific watchlist.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "watchlist_id": 1,
          "stock_id": 1,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        },
        {
          "id": 2,
          "watchlist_id": 1,
          "stock_id": 2,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        }
      ]
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Watchlist not found"
      }
      ```

### Delete Stock from Watchlist
- **DELETE /api/watchlists/:watchlist_id/stocks/:id**
  - Description: Deletes a specific stock from a watchlist.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "Stock deleted from watchlist successfully"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Watchlist or stock not found"
      }
      ```

## Algorithms

### Create Algorithm
- **POST /api/algorithms**
  - Description: Creates a new algorithm.
  - Request Body:
    - `name` (string): The name of the algorithm.
    - `description` (string): The description of the algorithm.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "Simple Moving Average",
        "description": "A simple moving average algorithm.",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Get Algorithm
- **GET /api/algorithms/:id**
  - Description: Retrieves details of a specific algorithm by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "Simple Moving Average",
        "description": "A simple moving average algorithm.",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Algorithm not found"
      }
      ```

### Get All Algorithms
- **GET /api/algorithms**
  - Description: Retrieves a list of all algorithms.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "user_id": 1,
          "name": "Simple Moving Average",
          "description": "A simple moving average algorithm.",
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        },
        {
          "id": 2,
          "user_id": 2,
          "name": "Exponential Moving Average",
          "description": "An exponential moving average algorithm.",
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        }
      ]
      ```

### Update Algorithm
- **PUT /api/algorithms/:id**
  - Description: Updates details of a specific algorithm by ID.
  - Request Body:
    - `name` (string): The new name of the algorithm.
    - `description` (string): The new description of the algorithm.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "user_id": 1,
        "name": "Updated Algorithm",
        "description": "An updated algorithm description.",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-20T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Algorithm not found"
      }
      ```

### Delete Algorithm
- **DELETE /api/algorithms/:id**
  - Description: Deletes a specific algorithm by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "Algorithm deleted successfully"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Algorithm not found"
      }
      ```

## Backtests

### Create Backtest
- **POST /api/backtests**
  - Description: Creates a new backtest for an algorithm.
  - Request Body:
    - `algorithm_id` (integer): The ID of the algorithm to backtest.
    - `start_date` (string): The start date of the backtest.
    - `end_date` (string): The end date of the backtest.
    - `initial_balance` (number): The initial balance for the backtest.
    - `final_balance` (number): The final balance after the backtest.
    - `profit_loss` (number): The profit/loss after the backtest.
    - `drawdown` (number): The drawdown percentage during the backtest.
    - `roi` (number): The return on investment percentage.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "algorithm_id": 1,
        "start_date": "2022-01-01",
        "end_date": "2022-12-31",
        "initial_balance": 10000.00,
        "final_balance": 10500.00,
        "profit_loss": 500.00,
        "drawdown": 2.5,
        "roi": 5.0,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Get Backtest
- **GET /api/backtests/:id**
  - Description: Retrieves details of a specific backtest by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "algorithm_id": 1,
        "start_date": "2022-01-01",
        "end_date": "2022-12-31",
        "initial_balance": 10000.00,
        "final_balance": 10500.00,
        "profit_loss": 500.00,
        "drawdown": 2.5,
        "roi": 5.0,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Backtest not found"
      }
      ```

### Get All Backtests
- **GET /api/backtests**
  - Description: Retrieves a list of all backtests.
  - Responses:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "algorithm_id": 1,
          "start_date": "2022-01-01",
          "end_date": "2022-12-31",
          "initial_balance": 10000.00,
          "final_balance": 10500.00,
          "profit_loss": 500.00,
          "drawdown": 2.5,
          "roi": 5.0,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        },
        {
          "id": 2,
          "algorithm_id": 2,
          "start_date": "2022-01-01",
          "end_date": "2022-12-31",
          "initial_balance": 15000.00,
          "final_balance": 15500.00,
          "profit_loss": 500.00,
          "drawdown": 3.0,
          "roi": 3.33,
          "created_at": "2023-06-19T00:00:00",
          "updated_at": "2023-06-19T00:00:00"
        }
      ]
      ```

### Update Backtest
- **PUT /api/backtests/:id**
  - Description: Updates details of a specific backtest by ID.
  - Request Body:
    - `start_date` (string): The new start date of the backtest.
    - `end_date` (string): The new end date of the backtest.
    - `initial_balance` (number): The new initial balance for the backtest.
    - `final_balance` (number): The new final balance after the backtest.
    - `profit_loss` (number): The new profit/loss after the backtest.
    - `drawdown` (number): The new drawdown percentage during the backtest.
    - `roi` (number): The new return on investment percentage.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "algorithm_id": 1,
        "start_date": "2022-01-01",
        "end_date": "2022-12-31",
        "initial_balance": 10000.00,
        "final_balance": 10500.00,
        "profit_loss": 500.00,
        "drawdown": 2.5,
        "roi": 5.0,
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-20T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Backtest not found"
      }
      ```

### Delete Backtest
- **DELETE /api/backtests/:id**
  - Description: Deletes a specific backtest by ID.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "Backtest deleted successfully"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": "Unauthorized access"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "errors": "Backtest not found"
      }
      ```

## Authentication

### Authenticate
- **GET /api/auth**
  - Description: Authenticates a user.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": {
          "message": "Unauthorized"
        }
      }
      ```

### Login
- **POST /api/auth/login**
  - Description: Logs a user in.
  - Request Body:
    - `email` (string): The email of the user.
    - `password` (string): The password of the user.
  - Responses:
    - 200 OK:
      ```json
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 401 Unauthorized:
      ```json
      {
        "errors": {
          "message": "Unauthorized"
        }
      }
      ```

### Logout
- **GET /api/auth/logout**
  - Description: Logs a user out.
  - Responses:
    - 200 OK:
      ```json
      {
        "message": "User logged out"
      }
      ```

### Signup
- **POST /api/auth/signup**
  - Description: Creates a new user and logs them in.
  - Request Body:
    - `username` (string): The username of the user.
    - `email` (string): The email of the user.
    - `password` (string): The password of the user.
  - Responses:
    - 201 Created:
      ```json
      {
        "id": 1,
        "username": "user1",
        "email": "user1@example.com",
        "created_at": "2023-06-19T00:00:00",
        "updated_at": "2023-06-19T00:00:00"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "errors": "Validation errors"
      }
      ```

### Unauthorized
- **GET /api/auth/unauthorized**
  - Description: Returns unauthorized JSON when flask-login authentication fails.
  - Responses:
    - 401 Unauthorized:
      ```json
      {
        "errors": {
          "message": "Unauthorized"
        }
      }
      ```

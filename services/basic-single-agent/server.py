"""
Calculator API Service - A simple calculator API using FastAPI
"""
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn
import argparse
import logging
from typing import Dict

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("calculator-api")

# Define API routes in a separate function for organization
def register_routes(app: FastAPI) -> None:
    """Register all API routes with the FastAPI application."""
    
    @app.get("/add", summary="Precisely adds two numbers together.", operation_id="add")
    async def add(a: float, b: float) -> Dict[str, float]:
        """Add two numbers and return the result."""
        logger.info(f"Adding {a} and {b}")
        return {"result": a + b}

    @app.get("/subtract", summary="Precisely subtracts two numbers.", operation_id="subtract")
    async def subtract(a: float, b: float) -> Dict[str, float]:
        """Subtract b from a and return the result."""
        logger.info(f"Subtracting {b} from {a}")
        return {"result": a - b}

    @app.get("/multiply", summary="Precisely multiplies two numbers.", operation_id="multiply")
    async def multiply(a: float, b: float) -> Dict[str, float]:
        """Multiply two numbers and return the result."""
        logger.info(f"Multiplying {a} and {b}")
        return {"result": a * b}

    @app.get("/divide", summary="Precisely divides two numbers.", operation_id="divide")
    async def divide(a: float, b: float) -> Dict[str, float]:
        """Divide a by b and return the result. Raises an error if b is 0."""
        logger.info(f"Dividing {a} by {b}")
        if b == 0:
            logger.error("Division by zero attempted")
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        return {"result": a / b}

# Error handlers
def register_exception_handlers(app: FastAPI) -> None:
    """Register exception handlers with the FastAPI application."""
    
    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        logger.error(f"Unhandled exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An unexpected error occurred. Please try again later."},
        )

def create_app(
    host: str = "127.0.0.1", 
    port: int = 8000, 
    description: str = "Calculator API Service",
    debug: bool = False
) -> FastAPI:
    """
    Factory function to create and configure a FastAPI application.
    
    Args:
        host: Host address to bind the server to
        port: Port to bind the server to
        description: API description text
        debug: Enable debug mode
    
    Returns:
        Configured FastAPI application
    """
    # Set log level based on debug flag
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        logger.debug("Debug mode enabled")
    
    # Create the server URL from host and port
    server_url = f"http://{host}:{port}"
    
    # Create FastAPI app with metadata
    app = FastAPI(
        title="Calculator API",
        description=description,
        version="1.0.0",
        servers=[
            {"url": server_url, "description": "Calculator API environment"},
        ],
        debug=debug,
    )
    
    # Add health check endpoint
    @app.get("/health", summary="Health check endpoint", tags=["system"])
    async def health_check() -> Dict[str, str]:
        """Return the health status of the API."""
        return {"status": "healthy"}
    
    # Register all components
    register_routes(app)
    register_exception_handlers(app)
    
    return app

def main() -> None:
    """Application entry point."""
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Run the Calculator API server")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the server on (default: 8000)")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host to run the server on (default: 127.0.0.1)")
    parser.add_argument("--description", type=str, default="Calculator API Service", 
                        help="Description for the API (default: 'Calculator API Service')")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    
    # Create the FastAPI app with the provided parameters
    app = create_app(
        host=args.host, 
        port=args.port, 
        description=args.description,
        debug=args.debug
    )
    
    # Start the server
    uvicorn.run(
        app, 
        host=args.host, 
        port=args.port,
        log_level="debug" if args.debug else "info"
    )

if __name__ == "__main__":
    main()
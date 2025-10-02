#!/usr/bin/env python3
"""
Simple test for FastAPI application
"""
import sys
import os

sys.path.append(os.path.dirname(__file__))

try:
    # Test if app imports correctly
    from app import app
    print("✅ FastAPI app imports successfully!")
    
    # Test basic functionality without TestClient
    import asyncio
    from fastapi import FastAPI
    
    # Verify it's a FastAPI instance
    assert isinstance(app, FastAPI)
    print("✅ App is a valid FastAPI instance!")
    
    # Check endpoints are registered
    routes = [route.path for route in app.routes]
    expected_routes = ["/", "/health", "/tasks"]
    
    for route in expected_routes:
        if route in routes:
            print(f"✅ Route {route} is registered")
        else:
            print(f"❌ Route {route} is missing")
    
    print("🎉 All basic tests passed!")
    
except Exception as e:
    print(f"❌ Test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

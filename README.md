flight-tracker/
├── config/
│   ├── settings.py          # API keys, coordinates, intervals
│   └── locations.json       # Preset locations 
├── src/
│   ├── api_client.py        # FlightRadar24 API wrapper
│   ├── data_processor.py    # Parse/clean flight data (regex, formatting)
│   ├── flight_detector.py   # Main loop, deduplication logic
│   └── notifier.py          # Send notifications (Pushover, Telegram, email?)
├── utils/
│   ├── logger.py            # Logging setup
│   └── geo.py               # Coordinate calculations, bounding boxes
├── tests/                   # Unit tests
├── main.py                  # Entry point
├── requirements.txt
├── .env.example             # Template for API keys
└── README.md
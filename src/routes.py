# A list of dictionaries to display all of the application's paths.
Routes = [
    {
        "endpoint": '/games',
        "description": 'Returns a list with all games',
        "parameters": [
            {
                "name": 'Videogame',
                "endpoint": '/games/<id>',
                "description": 'Returns all the information about a specific game'
            }
        ]
    },
    {
        "endpoint": '/companies',
        "description": 'Returns a list with all companies',
        "parameters": [
            {
                "name": 'Company',
                "endpoint": '/companies/<id>',
                "description": 'Returns all the information about a specific company'
            }
        ]
    },
    {
        "endpoint": '/photos',
        "description": 'Returns a list with all photos',
    }
]

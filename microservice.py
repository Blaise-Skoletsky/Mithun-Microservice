import zmq
import random

verb_ing_array = [
    "Running", "Jumping", "Swimming", "Reading", "Writing",
    "Singing", "Dancing", "Climbing", "Laughing", "Sleeping",
    "Eating", "Drinking", "Thinking", "Dreaming", "Talking",
    "Walking", "Hiking", "Biking", "Painting", "Drawing",
    "Cooking", "Baking", "Crying", "Smiling", "Studying",
    "Teaching", "Learning", "Creating", "Exploring", "Searching",
    "Discovering", "Playing", "Hugging", "Kissing", "Whispering",
    "Surfing", "Fishing", "Rowing", "Running", "Flying",
    "Hopping", "Skipping", "Glowing", "Falling", "Rising",
    "Shining", "Growing", "Sinking", "Riding", "Guiding",
    "Solving", "Waiting", "Wishing", "Falling", "Crawling",
    "Flying", "Caring", "Sharing", "Skiing", "Snowboarding",
    "Laughing", "Hunting", "Gathering", "Building", "Blossoming",
    "Babbling", "Chattering", "Cracking", "Roaring", "Hooting",
    "Giggling", "Humming", "Murmuring", "Whistling", "Exploding",
    "Melting", "Freezing", "Flourishing", "Quivering", "Spinning",
    "Dribbling", "Sliding", "Flickering", "Juggling", "Bouncing",
    "Rumbling", "Stumbling", "Fluttering", "Dwindling", "Wandering",
    "Rambling", "Tumbling", "Twinkling", "Unraveling", "Stirring",
    "Beaming", "Reflecting", "Confusing", "Revolving", "Dissolving",
    "Guiding"
]

adjective_array = [
    "Sparkling", "Vivacious", "Mysterious", "Enchanting", "Whimsical",
    "Resplendent", "Serene", "Exuberant", "Majestic", "Luminous",
    "Jubilant", "Tranquil", "Radiant", "Mystical", "Vibrant",
    "Captivating", "Gleaming", "Alluring", "Piquant", "Whimsical",
    "Ethereal", "Quirky", "Harmonious", "Dazzling", "Intriguing",
    "Scintillating", "Ornate", "Opulent", "Whirlwind", "Jubilant",
    "Effervescent", "Mesmerizing", "Enigmatic", "Astounding", "Resplendent",
    "Pulsating", "Enthralling", "Piquant", "Spirited", "Radiant",
    "Zesty", "Eloquent", "Dynamic", "Vivid", "Lively",
    "Sprightly", "Ethereal", "Quixotic", "Flamboyant", "Ephemeral",
    "Panoramic", "Aesthetic", "Sublime", "Grandiose", "Picturesque",
    "Opulent", "Serendipitous", "Irresistible", "Ineffable", "Enigmatic",
    "Mellifluous", "Zenith", "Lustrous", "Nebulous", "Quizzical",
    "Captivating", "Zephyr", "Pinnacle", "Iridescent", "Mellifluous",
    "Glorious", "Tantalizing", "Nebulous", "Ethereal", "Awe-inspiring",
    "Ineffable", "Illustrious", "Rhapsodic", "Rapt"
]
plural_noun_array = [
    "Apples", "Bananas", "Cherries", "Dogs", "Cats",
    "Horses", "Hats", "Books", "Keys", "Bottles",
    "Flowers", "Trees", "Rivers", "Mountains", "Oceans",
    "Puppies", "Kittens", "Children", "Friends", "Houses",
    "Cars", "Bicycles", "Watches", "Glasses", "Shoes",
    "Penguins", "Elephants", "Giraffes", "Lions", "Tigers",
    "Dinosaurs", "Butterflies", "Dragonflies", "Stars", "Clouds",
    "Computers", "Phones", "Cameras", "Monkeys", "Penguins",
    "Fish", "Whales", "Snakes", "Dragons", "Robots",
    "Aliens", "Kangaroos", "Koalas", "Pandas", "Pigs",
    "Chickens", "Cows", "Sheep", "Hens", "Roosters",
    "Frogs", "Turtles", "Snails", "Crabs", "Jellyfish",
    "Bears", "Deer", "Wolves", "Foxes", "Squirrels",
    "Bats", "Spiders", "Bees", "Ants", "Ladybugs",
    "Ducks", "Geese", "Swans", "Owls", "Eagles",
    "Seagulls", "Peacocks", "Penguins", "Kangaroos", "Zebras",
    "Pigs", "Goats", "Donkeys", "Rabbits", "Frogs",
    "Lions", "Tigers", "Bears", "Wolves", "Elephants",
    "Giraffes", "Monkeys", "Gorillas", "Birds", "Cats",
    "Dogs", "Snakes", "Fish", "Insects", "Reptiles"

]

places_array = [
    "Paris", "New York City", "Tokyo", "London", "Rome",
    "Sydney", "Rio de Janeiro", "Venice", "Barcelona", "Cairo",
    "Dubai", "Moscow", "Los Angeles", "Berlin", "Amsterdam",
    "Bangkok", "Istanbul", "Mumbai", "Cape Town", "Vancouver",
    "Santorini", "Bora Bora", "Kyoto", "Prague", "Vienna",
    "Toronto", "Seoul", "Buenos Aires", "Copenhagen", "Edinburgh",
    "Auckland", "Marrakech", "Havana", "Reykjavik", "Singapore",
    "Dublin", "Athens", "Helsinki", "Zurich", "Stockholm",
    "New Orleans", "San Francisco", "Munich", "Cancun", "Montreal",
    "Helsinki", "Oslo", "Perth", "Melbourne", "Hobart",
    "Florence", "Budapest", "Beijing", "Shanghai", "Cape Town",
    "Krakow", "Manhattan", "Quebec City", "Oxford", "Cambridge",
    "Seville", "Granada", "Valencia", "Ibiza", "Tahiti",
    "Galapagos Islands", "Bali", "Himalayas", "Great Barrier Reef", "Machu Picchu",
    "Amazon Rainforest", "Grand Canyon", "Yellowstone National Park", "Everest Base Camp", "Antarctica",
    "Dubrovnik", "Salzburg", "Bruges", "Nice", "Marseille",
    "Cologne", "Agra", "Jaipur", "Amritsar", "Bangalore",
    "Kolkata", "Hiroshima", "Nairobi", "Cairo", "Casablanca",
    "Kiev", "Warsaw", "Prague", "Bratislava", "Lisbon",
    "Bucharest", "Sofia", "Dublin", "Copenhagen", "Reykjavik",
    "Nairobi", "Cape Town", "Kigali", "Jerusalem", "Tbilisi"

]
body_parts_array = [
    "Head", "Shoulders", "Knees", "Toes", "Eyes",
    "Ears", "Nose", "Mouth", "Neck", "Chest",
    "Back", "Arms", "Elbows", "Hands", "Fingers",
    "Thumbs", "Hips", "Legs", "Knees", "Feet",
    "Toes", "Ankles", "Heels", "Toenails", "Fingernails",
    "Hair", "Eyebrows", "Eyelashes", "Forehead", "Jaw",
    "Cheeks"
    # ... (add more body parts as needed)
]




def randomizer(string):
    listVar = []
    match string:
        case 'verb':
            listVar = verb_ing_array
        case 'adjective':
            listVar = adjective_array
        case 'place':
            listVar = places_array
        case 'plural-noun':
            listVar = plural_noun_array
        case 'body':
            listVar = body_parts_array
        
    return random.choice(listVar)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    # Wait for next request from client
    message = socket.recv()

    # Call randomizer and send the result back to the client
    result = randomizer(message.decode('utf-8'))
    socket.send_string(result)
    print("Sent response: %s" % result)



from EmotionDetection.emotion_detection import emotion_detector

# Define a function to run unit tests
def run_unit_tests():
    # Test cases with statements and their expected dominant emotions
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]
    
    # Perform unit tests for each test case
    for statement, expected_emotion in test_cases:
        # Call the emotion_detector function with the statement
        result = emotion_detector(statement)
        
        # Print the result for debugging purposes
        print(f"Result for '{statement}': {result}")
        
        # Check if the dominant emotion matches the expected emotion
        if isinstance(result, dict) and result.get('dominant_emotion') == expected_emotion:
            print(f"Test passed for statement: '{statement}'")
        else:
            print(f"Test failed for statement: '{statement}'. Expected '{expected_emotion}', got '{result}'")

# Run the unit tests
run_unit_tests()
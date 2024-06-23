def sandwich_dressing(*dressings):
    print("This sandwich has :-")
    for dressing in dressings:
        
        print(f"- {dressing}")

sandwich_dressing('tomato', 'chicken', 'tuna')
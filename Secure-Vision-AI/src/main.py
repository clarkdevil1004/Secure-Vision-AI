from detect import run_detection

def main():
    print("=" * 45)
    print("      Secure Vision AI")
    print(" Real-Time Smart Surveillance System")
    print("=" * 45)
    print("Press 'Q' to exit.\n")

    run_detection(source=0)

if __name__ == "__main__":
    main()

import os
from dotenv import load_dotenv
import click
import uvicorn

@click.command()
@click.option(
    '--mode',
    type=click.Choice(['api', 'manual', 'test'], case_sensitive=False,),
    help="Run the app in 'api', 'manual', or 'test' mode."
)



def main(mode):
    # Load environment variables from .env
    load_dotenv(dotenv_path='.local.properties', override=True)
    
    # Get input and output directories from the environment variables
    # input_dir = os.getenv("SOURCE_DIR")
    # output_dir = os.getenv("OUTPUT_DIR")

    # os.makedirs(input_dir, exist_ok=True)
    # os.makedirs(output_dir, exist_ok=True)
    
    # Use match expression to handle different modes
    match mode.lower():
        case 'api':
            print("Running the API mode...")
            uvicorn.run('lib.fast_api:app', host="0.0.0.0", reload=True)
        
        case 'manual':...
        
        case 'test':...

if __name__ == "__main__":
    main()
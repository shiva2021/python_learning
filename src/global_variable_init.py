# %% [markdown]
# Lets learn how to set up environment variables

# %%
from dotenv import load_dotenv
import os

load_dotenv()

def getDotEnvs(envName):
    port = os.getenv(envName)
    print(port)

getDotEnvs("DB_PORT")

# %% [markdown]
# 



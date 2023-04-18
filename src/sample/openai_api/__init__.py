from sample.env_values import env
import openai


openai.api_key = env["OPENAI_API_KEY"]

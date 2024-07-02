""""""
import os
import uvicorn
from fastapi import FastAPI
from src.start import (classifier, 
                       parameters)
from src.config import logger, empty_result
from src.data_types import SearchData

os.environ["TOKENIZERS_PARALLELISM"] = "false"
app = FastAPI(title="ExpertBot-Sbert-T5")


@app.post("/api/search")
# @timeit
async def search(data: SearchData):
    """searching etalon by  incoming text"""
    logger.info("searched pubid: {} searched text: {}".format(str(data.pubid), str(data.text)))
    try:
        logger.info("searched text without spellcheck: {}".format(str(data.text)))
        result = await classifier.searching(str(data.text), data.pubid, parameters.sbert_score,
                                            parameters.t5_score, parameters.candidates_quantity)
        return result
    except Exception:
        logger.exception("Searching problem with text {} in pubid {}".format(str(data.text), str(data.pubid)))
        return empty_result

if __name__ == "__main__":
    uvicorn.run(app, host=parameters.host, port=parameters.port)

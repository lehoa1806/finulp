from news.article_filtering_stage import ArticleFilteringStage
from workflow.pipeline import Pipeline

from ..workflow import NewsScraperTask
from .articles_getting_stage import ArticlesGettingStage
from .scraper.thestar_scraper import TheStarScraper


class TheStarScrapingTask(NewsScraperTask):
    @property
    def pipeline(self) -> Pipeline:
        return Pipeline(
            stage=ArticlesGettingStage(
                scraper=TheStarScraper(headless=self.headless),
                max_pages_to_load=10,
            )
        ).add_stage(
            stage=ArticleFilteringStage(
                ft=self.filter,
                source='thestar.com.my',
            )
        )

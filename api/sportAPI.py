from flask_restful import Resource, reqparse, abort
import api.soccerAPI as soccer


class SoccerStats(Resource):
    def get(self, method):
        if method == 'prevstats':
            return soccer.load_prev_stats()
        elif method == 'predict':
            return soccer.load_predictions()
        elif method == 'update':
            soccer.update_stats()
            return '', 200
        else:
            abort(404, message='Route not found')


class SoccerDetails(Resource):
    def get(self, method, match_ID):
        if method == 'detailpredict':
            return soccer.get_details_to_prediction(match_ID)
        elif method == 'headtohead':
            return soccer.get_head_to_head_details(match_ID)
        elif method == 'awaylastten':
            return soccer.get_away_last_10(match_ID)
        elif method == 'homelastten':
            return soccer.get_home_last_10(match_ID)
        else:
            abort(404, message='Route not')

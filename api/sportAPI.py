from flask_restful import Resource, reqparse, abort
import api.soccerAPI as soccer

get_stats_args = reqparse.RequestParser()
get_stats_args.add_argument('match_ID', type=int, help='Id of the match')


class SoccerStats(Resource):
    def get(self, method):
        args = get_stats_args.parse_args()
        if method == 'prevstats':
            return soccer.load_prev_stats()
        elif method == 'predict':
            return soccer.load_predictions()
        elif method == 'update':
            soccer.update_stats()
            return '', 200
        elif method == 'detailpredict':
            return soccer.get_details_to_prediction(args['match_ID'])
        elif method == 'headtohead':
            return soccer.get_head_to_head_details(args['match_ID'])
        elif method == 'awaylastten':
            return soccer.get_away_last_10(args['match_ID'])
        elif method == 'homelastten':
            return soccer.get_home_last_10(args['match_ID'])
        else:
            abort(404, message='Route not found')

import requests
import random
import uuid
import time
from client import ask_bot


def post_to_facebook():
    token = ("EAAD6V7os0gcBO2tcXpaFApdjZBTutpmGiyX31Q0f1zPlSyJwZCpokwEwVfzvl7wT7MfB9o6DnbBOTNLXs4nw1lPcVpgre2iz8Qfcbm4vUiXBuOzt5WPEmvXGfoGTAsgkm7jM93J75Vn1PJ977BVtWz2xq4FRB8ohc6ooyr1UbMn9U8ZBuNNcZBNM6ERI6LIBdeloO6ZCV3H5LqN2ZB2AZDZD")
    client = f"{uuid.uuid4()}"
    uid = "61558511067110"
    question = "make a facebook post about tranding topic of bangladesh (skip politics) just give me the main text so i can post"
    text = ask_bot(question)

    headers = {
        "X-Fb-Ta-Logging-Ids": "graphql:cfcaff7a-b206-446a-a6ac-59f00eec3597",
        "X-Tigon-Is-Retry": "False",
        "Authorization": f"OAuth {token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Fb-Sim-Hni": "47001",
        "X-Fb-Background-State": "1",
        "X-Fb-Net-Hni": "47001",
        "X-Fb-Request-Analytics-Tags": '{"network_tags":{"product":"350685531728","purpose":"none",'
        '"request_category":"graphql","retry_attempt":"0"},'
        '"application_tags":"graphservice"}',
        "X-Graphql-Client-Library": "graphservice",
        "X-Fb-Friendly-Name": "ComposerStoryCreateMutation",
        "X-Fb-Privacy-Context": "496463117678580",
        "X-Fb-Navigation-Chain": "CreatorAdminComposerFragment,,,1690619321.840,3367078,,,;ComposerActivity,composer,"
        "tap_status_button,1690619286.310,68175353,,,;NewsFeedFragment,native_newsfeed,"
        "cold_start,1690619260.284,205388057,4748854339,,",
        "X-Fb-Device-Group": "4283",
        "User-Agent": "[FBAN/FB4A;FBAV/424.0.0.21.75;FBBV/495744378;FBDM/{density=2.75,width=1080,"
        "height=2241};FBLC/en_US;FBRV/498387158;FBCR/47001;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana"
        ";FBDV/2201116SG;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]",
        "X-Fb-Session-Id": "nid=KJ88DiL+HrFy;tid=78;nc=1;fc=1;bc=0;cid=8d26d179475c08d84072230c9afa3374",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Qpl-Active-Flows-Json": '{"schema_version":"v2","inprogress_qpls":[{"marker_id":25952257,"annotations":{'
        '"current_endpoint":"CreatorAdminComposerFragment"}}],"snapshot_attributes":{}}',
        "X-Fb-Rmd": "state=URL_ELIGIBLE",
        "Priority": "u=3, i",
        "Accept-Encoding": "gzip, deflate",
        "X-Fb-Http-Engine": "Liger",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Server-Cluster": "True",
        "X-Fb-Connection-Token": "8d26d179475c08d84072230c9afa3374",
    }

    variables = {
        "image_low_height": 2048,
        "image_medium_width": 540,
        "automatic_photo_captioning_enabled": "false",
        "angora_attachment_profile_image_size": 110,
        "poll_facepile_size": 110,
        "default_image_scale": "3",
        "image_high_height": 2048,
        "image_large_aspect_height": 565,
        "image_low_width": 360,
        "image_medium_height": 2048,
        "include_mentions_messenger_sharing_params": "true",
        "media_type": "image" "/jpeg",
        "size_style": "contain-fit",
        "image_high_width": 1080,
        "input": {
            "producer_supported_features": ["LIGHTWEIGHT_REPLY"],
            "tag_expansion_metadata": {"tag_expansion_ids": []},
            "place_attachment_setting": "SHOW_ATTACHMENT",
            "past_time": {"time_since_original_post": 0},
            "logging": {"composer_session_id": client},
            "camera_post_context": {
                "source": "COMPOSER",
                "platform": "FACEBOOK",
                "deduplication_id": client,
            },
            "connection_class": "EXCELLENT",
            "is_welcome_to_group_post": "false",
            "looking_for_players": {"selected_game": ""},
            "is_group_linking_post": "false",
            "is_throwback_post": "NOT_THROWBACK_POST",
            "is_boost_intended": "false",
            "navigation_data": {
                "attribution_id_v2": "CreatorAdminComposerFragment,,,1690619321.840,3367078,,,;ComposerActivity,c"
                "omposer,tap_status_button,1690619286.310,68175353,,,;NewsFeedFragment,nat"
                "ive_newsfeed,cold_start,1690619260.284,205388057,4748854339,,"
            },
            "reshare_original_post": "SHARE_LINK_ONLY",
            "idempotence_token": f"FEED_{client}",
            "composer_source_surface": "newsfeed",
            "composer_entry_picker": "NULL",
            "is_tags_user_selected": "false",
            "composer_session_events_log": {
                "number_of_keystrokes": 125,
                "number_of_copy_pastes": 0,
                "composition_duration": 45,
            },
            "message": {"text": text},
            "composer_entry_point": "inline_composer",
            "composer_type": "status",
            "nectar_module": "newsfeed_composer",
            "extensible_sprouts_ranker_request": {
                "RequestID": "a/BcCwABAAAAJGUyNDBmYjYyLTI3MjEtNDZhMS05NTExLWNiZTNhMDhhMmFlMwoAAgAAAABkxJY2CwADAA"
                "AACEFDVElWSVRZBgAEAAkLAAUAAAAZVU5ESVJFQ1RFRF9QQUdFU19DT01QT1NFUgA="
            },
            "audiences": [
                {
                    "undirected": {
                        "privacy": {
                            "tag_expansion_state": "UNSPECIFIED",
                            "deny": [],
                            "base_state": "EVERYONE",
                            "allow": [],
                        }
                    }
                }
            ],
            "is_thanks_group_post": "false",
            "source": "MOBILE",
            "actor_id": uid,
            "audiences_is_complete": "true",
            "action_timestamp": 1690619331,
        },
        "nt_context": {
            "using_white_navbar": "true",
            "pixel_ratio": 3,
            "is_push_on": "false",
            "styles_id": "2db8baac3fedcb28f8f867ad4cfda4ee",
            "bloks_version": "6b7b3f8082db05d75b681542674bfead5dffdb200860558d714d85c6254d966f",
        },
        "poll_voters_count": 5,
        "action_location": "feed",
        "include_image_ranges": "true",
        "profile_image_size": 110,
        "reading_attachment_profile_image_height": 371,
        "bloks_version": "6b7b3f8082db05d75b681542674bfead5dffdb200860558d714d85c6254d966f",
        "image_large_aspect_width": 1080,
        "reading_attachment_profile_image_width": 248,
        "profile_pic_media_type": "image/x-auto",
        "question_poll_count": 100,
        "angora_attachment_cover_image_size": 1320,
        "fetch_fbc_header": "true",
    }

    data = {
        "method": "post",
        "pretty": "false",
        "format": "json",
        "server_timestamps": "true",
        "locale": "en_US",
        "fb_api_req_friendly_name": "ComposerStoryCreateMutation",
        "fb_api_caller_class": "graphservice",
        "client_doc_id": "9109379062983427323922785397",
        "variables": f"{variables}",
        "fb_api_analytics_tags": '["visitation_id=4748854339:07d4d:1:1690619260.283","surface_hierarchy=ComposerFragment,'
        "null,null;ComposerActivity,composer,null;NewsFeedFragment,native_newsfeed,"
        'null;FbChromeFragment,null,cold_start;FbMainTabActivity,unknown,null",'
        '"session_id=UFS-904d949a-10aa-e825-6e2c-be813dfa65b4-fg-2","GraphServices"]',
        "client_trace_id": "cfcaff7a-b206-446a-a6ac-59f00eec3597",
    }

    for new in range(0, 10):
        resp = requests.post("https://graph.facebook.com/graphql", headers=headers, data=data)
        print(resp.text)


if __name__ == "__main__":
    while True:
        post_to_facebook()
        print("Waiting 60 seconds before next post...")
        time.sleep(60)
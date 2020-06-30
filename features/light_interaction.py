from instapy import smart_run


def light_interaction(session, photo_comments, u_followers, f_likers, f_tags):

    with smart_run(session):
        #
        # SET !
        #
        # Human like
        session.set_simulation(enabled=True,
                               percentage=66)
        session.set_action_delays(enabled=True,
                                  like=20,
                                  comment=60,
                                  follow=80,
                                  unfollow=120,
                                  randomize=True)
        # Quota supervisor
        session.set_quota_supervisor(enabled=True,
                                     sleep_after=["likes", "comments_d", "follows", "unfollows", "server_calls_h"],
                                     sleepyhead=True,
                                     stochastic_flow=True,
                                     notify_me=True,
                                     peak_likes_hourly=50,
                                     peak_likes_daily=585,
                                     peak_comments_hourly=25,
                                     peak_comments_daily=50,
                                     peak_follows_hourly=25,
                                     peak_follows_daily=None,
                                     peak_unfollows_hourly=20,
                                     peak_unfollows_daily=100,
                                     peak_server_calls_hourly=None,
                                     peak_server_calls_daily=4700)
        # Limits
        session.set_relationship_bounds(enabled=True,
                                        potency_ratio=None,
                                        delimit_by_numbers=True,
                                        max_followers=6000,
                                        max_following=3000,
                                        min_followers=30,
                                        min_following=30)
        # Fix comment section
        session.set_delimit_commenting(enabled=True,
                                       max_comments=10000,
                                       min_comments=0)
        # User interactions
        session.set_user_interact(amount=50,
                                  randomize=True,
                                  percentage=66)
        # # Likes
        session.set_do_like(enabled=True,
                            percentage=80)
        #Skip private account
        session.set_skip_users(skip_private=True,
                               private_percentage=100)
        # Follow settings
        session.set_do_follow(enabled=False,
                              percentage=75)
        # Comment settings
        session.set_do_comment(enabled=True,
                               percentage=40)
        session.set_comments(photo_comments)
        #
        # GO !
        #
        # Followers of
        session.interact_user_followers(u_followers,
                                        amount=15,
                                        randomize=False)
        # Liker's of
        session.follow_likers(f_likers,
                              photos_grab_amount=10,
                              follow_likers_per_photo=5,
                              randomize=True,
                              sleep_delay=900,
                              interact=True)
       # Follow by tag
        session.follow_by_tags(f_tags,
                               amount=50)
        # unfollow who doesnt follow you
        # session.unfollow_users(amount=50,
        #                        nonFollowers=True,
        #                        style="RANDOM",
        #                        unfollow_after=42 * 60 * 60,
        #                        sleep_delay=600)


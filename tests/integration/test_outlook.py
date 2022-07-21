from viadot.sources import Outlook
from viadot.config import local_config


def test_outlook_to_df():
    outlook_env_vars = local_config.get("OUTLOOK")
    outlook = Outlook(
        mailbox_name=outlook_env_vars["mail_example"],
        start_date="2022-06-28",
        end_date="2022-06-29",
    )
    df = outlook.to_df()
    assert df.shape[1] == 9
    assert df.empty == False

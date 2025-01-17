#  Copyright 2022-Present Autor contributors
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from autor.framework.activity_block import ActivityBlock
import click


@click.command()
@click.option(
    # pylint: disable-next=no-member
    "--flow-config-url",
    required=True,
    type=str,
    help="Flow Configuration file URL",
)
@click.option(
    # pylint: disable-next=no-member
    "--activity-block-id",
    required=True,
    type=str,
    help="The unique identifier of the activity block within the Flow Configuration",
)
@click.option(
    # pylint: disable-next=no-member
    "--flow-run-id",
    required=False,
    type=str,
    help="The unique identifier of a flow run. Generated by Autor if not provided as an argument."
)
def run(flow_config_url, activity_block_id, flow_run_id):
    # Get command-line parameters. Checks the mandatory params.
    activity_block = ActivityBlock(
        flow_config_url=flow_config_url,
        activity_block_id=activity_block_id,
        flow_run_id=flow_run_id,
    )
    activity_block.run()


if __name__ == "__main__":
    # Run the activity block
    run()

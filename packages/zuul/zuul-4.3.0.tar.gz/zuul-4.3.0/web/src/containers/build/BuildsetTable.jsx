// Copyright 2020 BMW Group
//
// Licensed under the Apache License, Version 2.0 (the "License"); you may
// not use this file except in compliance with the License. You may obtain
// a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
// WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
// License for the specific language governing permissions and limitations
// under the License.

import React from 'react'
import PropTypes from 'prop-types'
import { connect } from 'react-redux'
import {
  Button,
  EmptyState,
  EmptyStateBody,
  EmptyStateIcon,
  EmptyStateSecondaryActions,
  Spinner,
  Title,
} from '@patternfly/react-core'
import {
  BuildIcon,
  CodeBranchIcon,
  CodeIcon,
  CubeIcon,
  PollIcon,
  StreamIcon,
} from '@patternfly/react-icons'
import {
  Table,
  TableHeader,
  TableBody,
  TableVariant,
} from '@patternfly/react-table'

import { BuildResult, BuildResultWithIcon, IconProperty } from './Misc'
import { buildExternalTableLink } from '../../Misc'

function BuildsetTable({
  buildsets,
  fetching,
  onClearFilters,
  tenant,
  history,
}) {
  const columns = [
    {
      title: <IconProperty icon={<CubeIcon />} value="Project" />,
      dataLabel: 'Project',
    },
    {
      title: <IconProperty icon={<CodeBranchIcon />} value="Branch" />,
      dataLabel: 'Branch',
    },
    {
      title: <IconProperty icon={<StreamIcon />} value="Pipeline" />,
      dataLabel: 'Pipeline',
    },
    {
      title: <IconProperty icon={<CodeIcon />} value="Change" />,
      dataLabel: 'Change',
    },
    {
      title: <IconProperty icon={<PollIcon />} value="Result" />,
      dataLabel: 'Result',
    },
  ]

  function createBuildsetRow(buildset) {
    const changeOrRefLink = buildExternalTableLink(buildset)

    return {
      // Pass the buildset's uuid as row id, so we can use it later on in the
      // action handler to build the link to the build result page for each row.
      id: buildset.uuid,
      cells: [
        {
          // To allow passing anything else than simple string values to a table
          // cell, we must use the title attribute.
          title: (
            <BuildResultWithIcon
              result={buildset.result}
              link={`${tenant.linkPrefix}/buildset/${buildset.uuid}`}>
              {buildset.project}
            </BuildResultWithIcon>
          ),
        },
        {
          title: buildset.branch ? buildset.branch : buildset.ref,
        },
        {
          title: buildset.pipeline,
        },
        {
          title: changeOrRefLink && changeOrRefLink,
        },
        {
            title: (
              <BuildResult
                result={buildset.result}
                link={`${tenant.linkPrefix}/buildset/${buildset.uuid}`}
              >
              </BuildResult>
            ),
        },
      ],
    }
  }

  function createFetchingRow() {
    const rows = [
      {
        heightAuto: true,
        cells: [
          {
            props: { colSpan: 8 },
            title: (
              <center>
                <Spinner size="xl" />
              </center>
            ),
          },
        ],
      },
    ]
    return rows
  }

  let rows = []
  // For the fetching row we don't need any actions, so we keep them empty by
  // default.
  let actions = []
  if (fetching) {
    rows = createFetchingRow()
    // The dataLabel property is used to show the column header in a list-like
    // format for smaller viewports. When we are fetching, we don't want the
    // fetching row to be prepended by a "Project" column header. The other
    // column headers are not relevant here since we only have a single cell in
    // the fetching row.
    columns[0].dataLabel = ''
  } else {
    rows = buildsets.map((buildset) => createBuildsetRow(buildset))
    // This list of actions will be applied to each row in the table. For
    // row-specific actions we must evaluate the individual row data provided to
    // the onClick handler.
    actions = [
      {
        title: 'Show buildset result',
        onClick: (event, rowId, rowData) =>
          // The row's id contains the buildset's uuid, so we can use it to
          // build the correct link.
          history.push(`${tenant.linkPrefix}/buildset/${rowData.id}`),
      },
    ]
  }

  return (
    <>
      <Table
        aria-label="Builds Table"
        variant={TableVariant.compact}
        cells={columns}
        rows={rows}
        actions={actions}
        className="zuul-build-table"
      >
        <TableHeader />
        <TableBody />
      </Table>

      {/* Show an empty state in case we don't have any buildsets but are also
          not fetching */}
      {!fetching && buildsets.length === 0 && (
        <EmptyState>
          <EmptyStateIcon icon={BuildIcon} />
          <Title headingLevel="h1">No buildsets found</Title>
          <EmptyStateBody>
            No buildsets match this filter criteria. Remove some filters or
            clear all to show results.
          </EmptyStateBody>
          <EmptyStateSecondaryActions>
            <Button variant="link" onClick={onClearFilters}>
              Clear all filters
            </Button>
          </EmptyStateSecondaryActions>
        </EmptyState>
      )}
    </>
  )
}

BuildsetTable.propTypes = {
  buildsets: PropTypes.array.isRequired,
  fetching: PropTypes.bool.isRequired,
  onClearFilters: PropTypes.func.isRequired,
  tenant: PropTypes.object.isRequired,
  history: PropTypes.object.isRequired,
}

export default connect((state) => ({ tenant: state.tenant }))(BuildsetTable)

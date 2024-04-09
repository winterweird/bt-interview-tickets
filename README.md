# Bluetree interview case: Tickets

This is a small example project meant to be a simplified version of one of UpStacked's features. It's intended as a jumping-off point for a candidate to show how they would solve a given issue, in order to assess their problem-solving and communication skills. The case is divided in two parts: **Design** (where the candidate is asked open-ended questions about how they would solve a given technical challenge) and **implementation** (where the candidate prototypes an implementation of a small part of the solution).

The goal of this exercise is just to get an idea of the level of the candidate's technical expertise and problem solving ability, as well as their skills with the Python programming language and Django framework. There is no "one correct solution", and the candidate is not expected to necessarily know or solve everything. It's a given that the domain is more unfamiliar to them than the interviewers, but the candidate should be able to stake out a reasonable direction, reason about possible concerns/tradeoffs that might arise, and elaborate on their choices when prompted.

Estimated time: 1h

-   **Introductions:** 5-10m
-   **Short intro to the product:** 5m
-   **Problem description and setup:** 5-10m
-   **Design challenge:** 20m
-   **Coding challenge:** 20m
-   **Recap:** 5-10m

## Starting the server

```sh
$ docker compose up -d --build app   # to build and start
$ docker compose logs -f app         # to see logs
```

## Testing

You can test the server using http://localhost:8000/api/ (Swagger/OpenAPI docs), or test a particular endpoint with Spectacular's API inspection UI using http://localhost:8000/api/name_of_endpoint/. It's possible to set up required data in the database by logging in at http://localhost:8000/admin/. The username is `admin` and the password is `secret`.

## High level feature description

Customers should have the ability to report issues with their network infrastructures using these modes of communication:

-   Email (automatically created)
-   Phone call or email to support (ask an employee to register the issue)
-   Direct registration via system login (using a "customer user" account)

Employees need to be able to create issues on behalf of customers. Employees should be able to respond to the issues, customer would like to be notified. Employees should be able to track progress on resolving the issues.

Issues are given a priority, and depending on the priority there’s a set amount of time from issue creation you have to respond to the issue/assign it to someone, and a set amount of time you have to resolve it. Sometimes the issue is blocked by matters outside of your control (e.g. customer must respond), in which case we want to suspend the amount of time we have left for a set period of time.

When viewing an issue, we would like to see the following:

-   Reporter (may or may not be a system user)
-   Which network infrastructure the issue belongs to
-   Assignee (system user)
-   Status
-   Priority
-   Remaining time to assign (if applicable)
-   Remaining time to solve
-   Resolution ETA
-   Remaining suspended time (if applicable)
-   Resolution type (if applicable)

## Coding assignment

Assume you have a model «Ticket». How would you design an endpoint for updating ticket details? The endpoint should do the following:

-   Save the submitted JSON data. Must be able to:
    -   Change assignee
    -   Change status
    -   Change priority
-   Validate that the data is consistent, or automatically fix inconsistencies where applicable
    -   Remaining suspended time must be positive
    -   Assignee must be a registered employee-type user
    -   Ticket cannot have a «remaining suspended time» if not in a «suspended» state
    -   Those, and only those, tickets which are closed have resolution types
-   Add a required comment explaining the reason for the update
-   Respond appropriately to changes in priority - if the priority escalates, remaining time is reset according to new priority; if it de-escalates, remaining time is extended according to new priority
-   Notify any applicable people of the change

Don't be afraid to ask clarifying questions, bring up points you think of that aren't mentioned in the description, think out loud, etc. This is not only an assessment of your programming skills, but also your ability to communicate and collaborate, so involve your interviewer if you're uncertain about anything.

If there are changes required in the Ticket model or other supporting code, you're free to make those changes or assume they have been made for the purpose of solving this assignment. However, be reasonable: Don't just assume a method called `perform_update` has been defined!

### Additional questions

**Q:** How would you modify the Ticket model to include info about what causes the ticket to be pending? Possible causes:

-   Pending change
-   Pending customer
-   Pending third party
-   Pending closed (will be closed once pending time is over)

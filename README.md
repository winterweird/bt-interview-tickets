# Bluetree interview case: Tickets

## Starting the server

```sh
$ docker compose up -d --build app   # to build and start
$ docker compose logs -f app         # to see logs
```

## High level feature description

Customers should have the ability to report issues with their network infrastructures using these modes of communication:

-   Email
-   Phone call
-   Direct registration via system login

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

If there are changes required in the Ticket model or other supporting code, you're free to make those changes or assume they have been made for the purpose of solving this assignment. However, be reasonable: Don't just assume a method called `perform_update` has been defined!

### Additional questions

**Q:** How would you modify the Ticket model to include info about what causes the ticket to be pending? Possible causes:

-   Pending change
-   Pending customer
-   Pending third party
-   Pending closed (will be closed once pending time is over)

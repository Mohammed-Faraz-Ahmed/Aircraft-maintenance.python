"""
Aircraft Maintenance Tracking System
Tracks maintenance due hours for aircraft
"""

from datetime import datetime
from typing import List, Dict, Optional


class MaintenanceRecord:
    """Represents a single maintenance record"""

    def __init__(self, maintenance_type: str, due_hours: float, last_performed_hours: float = 0.0, last_performed_date: datetime = None):
        self.maintenance_type = maintenance_type
        self.due_hours = due_hours  # Hours between maintenance intervals
        self.last_performed_hours = last_performed_hours
        self.last_performed_date = last_performed_date or datetime.now()
        self.next_due_hours = last_performed_hours + due_hours

    def __str__(self):
        return f"{self.maintenance_type}: Due at {self.next_due_hours} hours"


class Aircraft:
    """Represents an aircraft with maintenance tracking"""

    def __init__(self, aircraft_id: str, aircraft_model: str, current_hours: float = 0.0):
        self.aircraft_id = aircraft_id
        self.aircraft_model = aircraft_model
        self.current_hours = current_hours
        self.maintenance_records: Dict[str, MaintenanceRecord] = {}
        self.maintenance_history: List[Dict] = []

    def add_maintenance_schedule(self, maintenance_type: str, due_hours: float,
                                last_performed_hours: float = 0.0,
                                last_performed_date: datetime = None) -> None:
        """Add a maintenance schedule for the aircraft"""
        record = MaintenanceRecord(maintenance_type, due_hours, last_performed_hours, last_performed_date)
        self.maintenance_records[maintenance_type] = record

    def update_aircraft_hours(self, new_hours: float) -> None:
        """Update the current flight hours of the aircraft"""
        if new_hours < self.current_hours:
            print(f"Warning: New hours ({new_hours}) cannot be less than current hours ({self.current_hours})")
            return
        self.current_hours = new_hours

    def get_maintenance_due(self) -> List[Dict]:
        """Get all maintenance that is currently due or overdue"""
        due_maintenance = []
        for maintenance_type, record in self.maintenance_records.items():
            if self.current_hours >= record.next_due_hours:
                hours_overdue = self.current_hours - record.next_due_hours
                due_maintenance.append({
                    'type': maintenance_type,
                    'due_hours': record.next_due_hours,
                    'current_hours': self.current_hours,
                    'hours_overdue': hours_overdue,
                    'status': 'OVERDUE' if hours_overdue > 0 else 'DUE'
                })
        return due_maintenance

    def get_maintenance_schedule(self) -> List[Dict]:
        """Get the maintenance schedule sorted by urgency (hours until due)"""
        schedule = []
        for maintenance_type, record in self.maintenance_records.items():
            hours_until_due = record.next_due_hours - self.current_hours
            schedule.append({
                'type': maintenance_type,
                'next_due_hours': record.next_due_hours,
                'current_hours': self.current_hours,
                'hours_until_due': hours_until_due,
                'due_interval': record.due_hours
            })

        # Sort by hours until due (ascending)
        schedule.sort(key=lambda x: x['hours_until_due'])
        return schedule

    def perform_maintenance(self, maintenance_type: str) -> bool:
        """Mark maintenance as completed"""
        if maintenance_type not in self.maintenance_records:
            print(f"Maintenance type '{maintenance_type}' not found")
            return False

        record = self.maintenance_records[maintenance_type]
        record.last_performed_hours = self.current_hours
        record.last_performed_date = datetime.now()
        record.next_due_hours = self.current_hours + record.due_hours

        # Log to history
        self.maintenance_history.append({
            'type': maintenance_type,
            'performed_hours': self.current_hours,
            'performed_date': record.last_performed_date,
            'next_due_hours': record.next_due_hours
        })

        print(f"✓ {maintenance_type} completed at {self.current_hours} hours")
        print(f"  Next {maintenance_type} due at {record.next_due_hours} hours")
        return True

    def get_hours_until_maintenance(self, maintenance_type: str) -> Optional[float]:
        """Get hours remaining until specific maintenance is due"""
        if maintenance_type not in self.maintenance_records:
            return None

        record = self.maintenance_records[maintenance_type]
        hours_until = record.next_due_hours - self.current_hours
        return max(0, hours_until)

    def display_status(self) -> None:
        """Display current maintenance status"""
        print(f"\n========== Aircraft: {self.aircraft_id} ({self.aircraft_model}) ==========")
        print(f"Current Flight Hours: {self.current_hours}\n")

        # Display overdue maintenance
        due = self.get_maintenance_due()
        if due:
            print("⚠️  OVERDUE/DUE MAINTENANCE:")
            for item in due:
                print(f"   • {item['type']}: {item['hours_overdue']:.1f} hours overdue (due at {item['due_hours']:.1f}h)")

        # Display upcoming maintenance
        print("\n📅 UPCOMING MAINTENANCE:")
        schedule = self.get_maintenance_schedule()
        for item in schedule[:5]:  # Show top 5
            status = "🔴 NOW" if item['hours_until_due'] <= 0 else f"({item['hours_until_due']:.1f}h)"
            print(f"   • {item['type']}: Due at {item['next_due_hours']:.1f}h {status}")

        print()

    def get_maintenance_report(self) -> Dict:
        """Generate a comprehensive maintenance report"""
        return {
            'aircraft_id': self.aircraft_id,
            'aircraft_model': self.aircraft_model,
            'current_hours': self.current_hours,
            'due_maintenance': self.get_maintenance_due(),
            'maintenance_schedule': self.get_maintenance_schedule(),
            'maintenance_history': self.maintenance_history
        }


def main() -> None:
    """Example usage of the Aircraft Maintenance Tracking System"""

    # Create an aircraft
    aircraft = Aircraft("N12345", "Boeing 737", current_hours=5000)

    # Add maintenance schedules
    aircraft.add_maintenance_schedule("Oil Change", due_hours=100, last_performed_hours=4900)
    aircraft.add_maintenance_schedule("Tire Inspection", due_hours=500, last_performed_hours=4500)
    aircraft.add_maintenance_schedule("Engine Overhaul", due_hours=2000, last_performed_hours=4000)
    aircraft.add_maintenance_schedule("Hydraulic System Check", due_hours=250, last_performed_hours=4750)
    aircraft.add_maintenance_schedule("Avionics Update", due_hours=1000, last_performed_hours=4000)

    # Display initial status
    aircraft.display_status()

    # Simulate flight operations
    print("--- Simulating 50 flight hours ---")
    aircraft.update_aircraft_hours(5050)
    aircraft.display_status()

    # Perform maintenance
    print("--- Performing Oil Change ---")
    aircraft.perform_maintenance("Oil Change")
    aircraft.display_status()

    # Another flight
    print("--- Simulating 200 more flight hours ---")
    aircraft.update_aircraft_hours(5250)
    aircraft.display_status()

    # Get specific maintenance info
    print("--- Checking specific maintenance ---")
    hours_until_engine = aircraft.get_hours_until_maintenance("Engine Overhaul")
    print(f"Hours until Engine Overhaul: {hours_until_engine}")

    # Generate report
    print("\n--- Maintenance Report ---")
    report = aircraft.get_maintenance_report()
    print(f"Aircraft: {report['aircraft_id']} ({report['aircraft_model']})")
    print(f"Current Hours: {report['current_hours']}")
    print(f"Critical Maintenance Due: {len(report['due_maintenance'])} item(s)")


if __name__ == "__main__":
    main()

